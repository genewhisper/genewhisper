def pathogenicity(item):
    strong_criterias = [item["PS1"], item["PS2"], item["PS3"], item["PS4"]]
    moderate_criterias = [item["PM1"], item["PM2"], item["PM3"], item["PM4"], item["PM5"], item["PM6"]]
    supporting_criterias = [item["PP1"], item["PP2"], item["PP3"], item["PP4"], item["PP5"]]

    print(moderate_criterias)
    print ((moderate_criterias).count(False), (moderate_criterias).count(True), (moderate_criterias).count("TBD"))
    try:
        #Pathogenic
        #case I
        #(a)
        if((item["PVS1"] == True) and ((strong_criterias).count(True)>=1)):
            return "Pathogenic, I-a"

        #(b)
        elif((item["PVS1"] == True) and ((moderate_criterias).count(True)>=2)):
            return "Pathogenic, I-b"

        #(c)
        elif((item["PVS1"] == "TBD") and ((moderate_criterias).count(True)==1 and (supporting_criterias).count(True)==1)):
            return "Pathogenic, I-c"

        #(d)
        elif((item["PVS1"] == True) and ((supporting_criterias).count(True)>=2)):
            return "Pathogenic, I-d"

        #case II
        elif(strong_criterias.count(True)>=2):
            return "Pathogenic, II"

        #case III
        #(a)
        elif((strong_criterias.count(True)==1) and (moderate_criterias.count(True)>=3)):
            return "Pathogenic, III-a"

        #(b)
        elif((moderate_criterias.count(True)==2) and (supporting_criterias.count(True)>=2)):
            return "Pathogenic, III-b"

        #(c)
        elif((moderate_criterias.count(True)==1) and (supporting_criterias.count(True)>=4)):
            return "Pathogenic, III-c"

        #Likely Pathogenic
        #case I
        if((item["PVS1"] == True) and ((moderate_criterias).count(True)==1)):
            return "Likely_pathogenic, I"

        #case II
        elif((strong_criterias.count(True)==1) and (moderate_criterias.count(True)==(1 or 2))):
            return "Likely_pathogenic, II"

        #case III
        elif((strong_criterias.count(True)==1) and (supporting_criterias.count(True)>=2)):
            return "Likely_pathogenic, III"

        #case IV
        elif(moderate_criterias.count(True)>=3):
            return "Likely_pathogenic, IV"

        #case V
        elif((moderate_criterias.count(True)==2) and (supporting_criterias.count(True)>=2)):
            return "Likely_pathogenic, V"

        #case VI
        elif((moderate_criterias.count(True)==1) and (supporting_criterias.count(True)>=4)):
            return "Likely_pathogenic, VI"

        #Benign
        #case I
        elif(item["BA1"] == True):
            return "Benign, I"

        #case II
        elif(strong_criterias.count(True)>=2):
            return "Benign, II"

        #Likely benign
        #case I
        elif((strong_criterias.count(True)==1) and (supporting_criterias.count(True)==1)):
            return "Likely_benign, I"

        #case II
        elif(supporting_criterias.count(True)>=2):
            return "Likely_benign, II"
        else:
            return "Uncertain_significance"

    except (ValueError, TypeError):
        return "Empty"
