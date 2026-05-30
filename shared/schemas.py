from pydantic import BaseModel
from typing import Optional
from enum import Enum


# --- Signal Extraction ---

class SignalExtractionInput(BaseModel):
    raw_content: str


class SignalExtractionOutput(BaseModel):
    signals: list[str]
    themes: list[str]
    quotable_facts: list[str]


# --- Audience Reasoning ---

class AudienceReasoningInput(BaseModel):
    signals: list[str]
    themes: list[str]


class Audience(BaseModel):
    segment: str
    relevance_reason: str


class AudienceReasoningOutput(BaseModel):
    audiences: list[Audience]
    recommended_icp: str


# --- Customer Profile ---

class CustomerProfileInput(BaseModel):
    recommended_icp: str
    signals: list[str]


class CustomerProfileOutput(BaseModel):
    persona: str
    pain_points: list[str]
    buying_trigger: str
    relevance_score: int  # 1-10
    assumptions: list[str]


# --- Outreach Method ---

class OutreachMethodEnum(str, Enum):
    linkedin_post = "linkedin_post"
    email = "email"
    website_block = "website_block"
    faq = "faq"
    snippet = "snippet"
    hubspot_note = "hubspot_note"
    sales_talking_points = "sales_talking_points"


class OutreachMethodInput(BaseModel):
    persona: str
    signals: list[str]


class OutreachMethodOutput(BaseModel):
    method: OutreachMethodEnum
    rationale: str
    required_sections: list[str]


# --- Executing Agent ---

class ExecutingAgentInput(BaseModel):
    method: OutreachMethodEnum
    persona: str
    signals: list[str]


class ExecutingAgentOutput(BaseModel):
    generation_plan: str
    tone: str
    cta: str
    missing_inputs: list[str]


# --- Message Formatting ---

class MessageFormattingInput(BaseModel):
    generation_plan: str
    persona: str
    tone: str
    cta: str


class MessageFormattingOutput(BaseModel):
    copy: str
    headline: str
    cta: str
    grounded_claims: list[str]
    warnings: list[str]


# --- Graphical Pipeline ---

class GraphicalPipelineInput(BaseModel):
    generation_plan: str
    persona: str
    method: OutreachMethodEnum


class GraphicalPipelineOutput(BaseModel):
    style_direction: str
    layout_notes: str
    image_prompt: str


# --- Representation ---

class RepresentationInput(BaseModel):
    persona: str
    pain_points: list[str]
    buying_trigger: str
    relevance_score: int
    assumptions: list[str]
    method: OutreachMethodEnum
    copy: str
    headline: str
    cta: str
    grounded_claims: list[str]
    warnings: list[str]
    style_direction: str
    image_prompt: str


class ValidationSummary(BaseModel):
    grounded_claims: list[str]
    unverified_assumptions: list[str]
    human_review_required: list[str]
    confidentiality_risks: list[str]


class RepresentationOutput(BaseModel):
    customer_profile: dict
    selected_method: str
    message_asset: dict
    visual_direction: dict
    validation_summary: ValidationSummary
    human_confirmation_status: str  # "pending" | "approved" | "rejected"
