def pathogenicity(item):
    strong_criterias = [item["PS1"], item["PS2"], item["PS3"], item["PS4"]]
    moderate_criterias = [
        item["PM1"], item["PM2"], item["PM3"], item["PM4"], item["PM5"],
        item["PM6"]
    ]

    supporting_criterias = [
        item["PP1"], item["PP2"], item["PP3"], item["PP4"], item["PP5"]
    ]

    try:

        #Pathogenic
        #case I
        #(a)
        if ((item["PVS1"] == True) and ((strong_criterias).count(True) >= 1)):
            return [
                "Pathogenic",
                "1 Very strong (PVS1) AND (a) >=1 Strong (PS1–PS4)"
            ]
        #(b)
        elif ((item["PVS1"] == True) and
              ((moderate_criterias).count(True) >= 2)):
            return [
                "Pathogenic", "1 Very strong (PVS1) AND >=2 Moderate (PM1–PM6)"
            ]
        #(c)
        elif ((item["PVS1"] == True) and
              ((moderate_criterias).count(True) == 1 and
               (supporting_criterias).count(True) == 1)):
            return [
                "Pathogenic",
                ("1 Very strong (PVS1) AND (1 Moderate (PM1–PM6) "
                 "AND 1 supporting (PP1–PP5))")
            ]
        #(d)
        elif ((item["PVS1"] == True) and
              ((supporting_criterias).count(True) >= 2)):
            return [
                "Pathogenic",
                "1 Very strong (PVS1) AND >=2 Supporting (PP1–PP5)"
            ]

        #case II
        elif (strong_criterias.count(True) >= 2):
            return ["Pathogenic", ">=2 Strong (PS1–PS4)"]

        #case III
        #(a)
        elif ((strong_criterias.count(True) == 1) and
              (moderate_criterias.count(True) >= 3)):
            return [
                "Pathogenic", "1 Strong (PS1–PS4) AND >=3 Moderate (PM1–PM6)"
            ]

        #(b)
        elif ((strong_criterias.count(True) == 1) and
              (moderate_criterias.count(True) == 2) and
              (supporting_criterias.count(True) >= 2)):
            return [
                "Pathogenic",
                ("1 Strong (PS1–PS4) AND 2 Moderate (PM1–PM6) "
                 "AND >=2 Supporting (PP1–PP5)")
            ]

        #(c)
        elif ((strong_criterias.count(True) == 1) and
              (moderate_criterias.count(True) == 1) and
              (supporting_criterias.count(True) >= 4)):
            return [
                "Pathogenic",
                ("1 Strong (PS1–PS4) "
                 "AND 1 Moderate (PM1–PM6) "
                 "AND >=4 supporting (PP1–PP5)")
            ]

        #Likely Pathogenic
        #case I
        if ((item["PVS1"] == True) and
            ((moderate_criterias).count(True) == 1)):
            return [
                "Likely_pathogenic",
                "1 Very strong (PVS1) AND 1 moderate (PM1–PM6)"
            ]

        #case II
        elif ((strong_criterias.count(True) == 1) and
              (moderate_criterias.count(True) == (1 or 2))):
            return [
                "Likely_pathogenic",
                "1 Strong (PS1–PS4) AND 1–2 moderate (PM1–PM6)"
            ]

        #case III
        elif ((strong_criterias.count(True) == 1) and
              (supporting_criterias.count(True) >= 2)):
            return [
                "Likely_pathogenic",
                "1 Strong (PS1–PS4) AND >=2 supporting (PP1–PP5) OR"
            ]

        #case IV
        elif (moderate_criterias.count(True) >= 3):
            return ["Likely_pathogenic", ">=3 Moderate (PM1–PM6)"]

        #case V
        elif ((moderate_criterias.count(True) == 2) and
              (supporting_criterias.count(True) >= 2)):
            return [
                "Likely_pathogenic",
                "2 Moderate (PM1–PM6) AND >=2 supporting (PP1–PP5)"
            ]

        #case VI
        elif ((moderate_criterias.count(True) == 1) and
              (supporting_criterias.count(True) >= 4)):
            return [
                "Likely_pathogenic",
                "1 Moderate (PM1–PM6) AND >=4 supporting (PP1–PP5)"
            ]

        #Benign
        #case I
        elif ((item["BA1"] == True) and (item["PVS1"] == (False or "TBD")) and
              (any(x == (False or "TBD") for x in moderate_criterias)) and
              (any(x == (False or "TBD") for x in strong_criterias)) and
              (any(x == (False or "TBD") for x in supporting_criterias))):
            return ["Benign", "1 Stand-alone (BA1)"]

        #case II
        elif (strong_criterias.count(True) >= 2):
            return ["Benign", ">=2 Strong (BS1–BS4)"]

        #Likely benign
        #case I
        elif ((strong_criterias.count(True) == 1) and
              (supporting_criterias.count(True) == 1)):
            return [
                "Likely_benign",
                "1 Strong (BS1–BS4) and 1 supporting (BP1–BP7)"
            ]

        #case II
        elif (supporting_criterias.count(True) >= 2):
            return ["Likely_benign", ">= Supporting (BP1–BP7)"]

        else:
            return [
                "Uncertain_significance",
                ("Other criteria shown above are not met OR "
                 "the criteria for benign and pathogenic are contradictory")
            ]

    except (ValueError, TypeError):
        return None
