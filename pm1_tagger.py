
def pm1_filter(item):
    """
    Takes an Oncotator database row, and returns True/False
    for whether item is PM1.
    """
    
    if (item["UniProt_Region"] and
        item["Varient_Classification"] == "Missense_Mutation"):
        return True
    else:
        return False


    
