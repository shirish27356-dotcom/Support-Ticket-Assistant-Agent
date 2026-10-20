import json
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm import get_model


# ---------- Step 1: triage (structured output) ----------
class Ticket(BaseModel):
    category: Literal["billing", "technical", "account", "other"] = Field(
        description="Best matching category"
    )
    urgency: Literal["low", "medium", "high"] = Field(description="How urgent the problem is")
    summary: str = Field(description="One sentence summary of the problem")

model = get_model()

classifier_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Classify the customer message by category, urgency, and summary."),
        ("human", "{question}"),
    ]
)
classifier = classifier_prompt | model.with_structured_output(Ticket)


def make_reply_chains(instruction):

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", instruction),
            ("human", "{ticket}"),
        ]
    )
    return prompt | model | StrOutputParser()

billing_chain = make_reply_chains(
    "You are a helpful assistant that can answer billing questions. "
)

account_chain = make_reply_chains(
    "You are a helpful assistant that can answer account questions. "
)

other_chain = make_reply_chains(
    "You are a helpful assistant that can answer general questions. ")

def route_ticket(ticket: Ticket):
    if ticket.category == "billing":
        return billing_chain
    elif ticket.category == "account":
        return account_chain
    else:
        return other_chain


def process_ticket(question): 
    ticket = classifier.invoke({"question": question})
    print(f"Ticket: {ticket.model_dump_json()}")
    reply_chain = route_ticket(ticket)
    reply = reply_chain.invoke({"ticket": question})

    return {

        "ticket": ticket.model_dump_json(),
        "reply": reply,
        "summary": ticket.summary,
        "urgency": ticket.urgency,
        "category": ticket.category,
        "customer_message" : question
    }

if __name__ == "__main__":
    question = input("Customer message: ")

    try:
        result = process_ticket(question)
        print(json.dumps(result, indent=2))

        path = Path("ticket_result.json")
        records = json.loads(path.read_text()) if path.exists() else []

        records.append(result)
        path.write_text(json.dumps(records, indent=2))

        print(f"Result saved to {path.resolve()}")

    except Exception as e:
        print(f"Error processing ticket: {e}")
