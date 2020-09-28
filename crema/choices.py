from enum import Enum


class EventType(Enum):
    # PSCORE
    USER = "USER"
    LOAN_APPLICATION = "LOAN_APPLICATION"
    DOCUMENT = "DOCUMENT"
    LOAN = "LOAN"
    USER_INFO_REQUEST = "USER_INFO_REQUEST"
    EMPLOYMENT = "EMPLOYMENT"
    DEBIT_INSTRUCTION = "DEBIT_INSTRUCTION"
    ADDRESS = "ADDRESS"
    BANK_ACCOUNT = "BANK_ACCOUNT"
    INCOME_VERIFICATION = "INCOME_VERIFICATION"
    USER_REFERENCES = "USER_REFERENCES"
    ASSISTANCE_REMINDER = "ASSISTANCE_REMINDER"
    ASSISTANCE_ACTIVITY = "ASSISTANCE_ACTIVITY"
    WHATSAPP_COMM = "WHATSAPP_COMM"
    OPS_COMMENT = "OPS_COMMENT"
    SMS = "SMS"
    ASSISTANCE_AGENT_CALL = "ASSISTANCE_AGENT_CALL"
    DEVICE_INSTALLATION = "DEVICE_INSTALLATION"
    USER_AGENT_ASSIGNMENT = "USER_AGENT_ASSIGNMENT"
    ASSISTANCE_USER_TAG = "ASSISTANCE_USER_TAG"
    LOAN_RESTRUCTURE = "LOAN_RESTRUCTURE"

    # AMS
    ASSESSMENT = "ASSESSMENT"
    PRODUCT_ELIGIBILITY = "PRODUCT_ELIGIBILITY"
    BUREAU_ADDRESS = "BUREAU_ADDRESS"

    # NBFC AMS
    NBFC_ASSESSMENT = "NBFC_ASSESSMENT"

    # USER_ACTIVITY
    USER_ACTIVITY = "USER_ACTIVITY"

    # PAYMENTS
    LOAN_INFO_STATIC = "LOAN_INFO_STATIC"
    LOAN_INFO_DYNAMIC = "LOAN_INFO_DYNAMIC"
    VIRTUAL_ACCOUNT = "VIRTUAL_ACCOUNT"

    # INTERNAL TOPICS
    # All internal topics start with prefix I_
    I_LOAN_APPLICATION_INDEX = "I_LOAN_APPLICATION_INDEX"
    I_LEAD_INDEX = "I_LEAD_INDEX"
    I_SALES_FORCE = "I_SALES_FORCE"
    I_CLEVER_TAP = "I_CLEVER_TAP"


class EventPartition(Enum):
    # PSCORE
    USER = 16
    LOAN_APPLICATION = 16
    DOCUMENT = 8
    LOAN = 8
    USER_INFO_REQUEST = 8
    EMPLOYMENT = 8
    DEBIT_INSTRUCTION = 8
    ADDRESS = 8
    BANK_ACCOUNT = 8
    INCOME_VERIFICATION = 8
    USER_REFERENCES = 8
    ASSISTANCE_REMINDER = 8
    ASSISTANCE_ACTIVITY = 16
    WHATSAPP_COMM = 8
    OPS_COMMENT = 8
    SMS = 8
    ASSISTANCE_AGENT_CALL = 8
    DEVICE_INSTALLATION = 8
    USER_AGENT_ASSIGNMENT = 8
    ASSISTANCE_USER_TAG = 8
    LOAN_RESTRUCTURE = 8

    # AMS
    ASSESSMENT = 16
    PRODUCT_ELIGIBILITY = 8
    BUREAU_ADDRESS = 8

    # NBFC AMS
    NBFC_ASSESSMENT = 16

    # USER_ACTIVITY
    USER_ACTIVITY = 128

    # PAYMENTS
    LOAN_INFO_STATIC = 8
    LOAN_INFO_DYNAMIC = 32
    VIRTUAL_ACCOUNT = 8

    # INTERNAL TOPICS
    I_LOAN_APPLICATION_INDEX = 64
    I_LEAD_INDEX = 64
    I_SALES_FORCE = 64
    I_CLEVER_TAP = 64
