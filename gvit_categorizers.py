def PM1(item):
    """
    Located in a mutational hot spot and/or critical and
    well-established functional domain (e.g., active
    site of an enzyme) without benign variation
    """
    if (item["UniProt_Region"] and
            item["Variant_Classification"] == "Missense_Mutation"):
        return True
    else:
        return False


def PM2(item):
    """
    Absent from controls (or at extremely low frequency if recessive) in
    Exome Sequencing Project, 1000 Genomes Project, or
    Exome Aggregation Consortium

    Apply PM2 if one of the following is disease causing
    ExAC_AF: anything < 0.005 to absent is disease-causing
    1000gp3_AF: anything < 0.005 to absent is disease-causing
    """
    try:
        if (float(item["ExAC_AF"]) < 0.005 and
                float(item["1000gp3_AF"]) < 0.005):
            return False
        else:
            return True

    except (ValueError, TypeError):
        return "TBD"


def PVS1(item):
    """
    null variant (nonsense, frameshift, canonical ±1 or 2 splice sites,
    initiation codon, single or multiexon deletion) in a gene
    where LOF is a known mechanism of disease.

    PVS1 null variant (nonsense, frameshift,
    canonical ±1 or 2 splice sites, initiation codon,
    single or multiexon deletion) in a gene where LOF
    is a known mechanism of disease.
    Caveats:
      - Beware of genes where LOF is not a known
        disease mechanism (e.g., GFAP, MYH7)
      - Use caution interpreting LOF variants
        at the extreme 3′ end of a gene
      - Use caution with splice variants that are
        predicted to lead to exon skipping but
        leave the remainder of the  protein intact
      - Use caution in the presence of multiple
        transcripts
    """
    if (item["Variant_Classification"] in [
            "Nonsense_Mutation"
            "Frame_Shift_Ins", "Frame_Shift_Del"
    ]):
        return True
    elif (item["Variant_Classification"] in [
            "Intron", "5'UTR", "3'UTR", "IGR", "5'Flank", "Missense_Mutation"
    ]):
        return False
    else:
        return "TBD"


def PS1(item):
    """
    Same amino acid change as a previously established pathogenic
    variant regardless of nucleotide change
    """
    pass


def PS2(item):
    """
    De novo (both maternity and paternity confirmed) in a patient with the
    disease and no family history
    """
    pass


def PS3(item):
    """
    Well-established in vitro or in vivo functional studies supportive of
    a damaging effect on the gene or gene product
    """
    pass


def PS4(item):
    """
    The prevalence of the variant in affected individuals is
    significantly increased compared with the prevalence in controls
    """
    pass


def PP1(item):
    """
    (Strong evidence) Cosegregation with disease in multiple affected
    family members in a gene definitively known to cause the disease
    """
    pass


def PM3(item):
    """
    For recessive disorders, detected in trans with a
    pathogenic variant
    """
    pass


def PM4(item):
    """
    Protein length changes as a result of in-frame deletions/insertions in
    a nonrepeat region or stop-loss variants
    """
    pass


def PM5(item):
    """
    Novel missense change at an amino acid residue where a different
    missense change determined to be pathogenic has been seen before
    """
    pass


def PM6(item):
    """
    Assumed de novo, but without confirmation of paternity
    and maternity
    """
    pass


def PP1(item):
    """
    (Moderate evidence) Cosegregation with disease in multiple affected
    family members in a gene definitively known to cause the disease
    """
    pass


def PP1(item):
    """
    Cosegregation with disease in multiple affected family members in a
    gene definitively known to cause the disease
    """
    pass


def PP2(item):
    """
    Missense variant in a gene that has a low rate of benign missense
    variation and in which missense variants are a
    common mechanism of disease
    """
    pass


def PP3(item):
    """
    Multiple lines of computational evidence support a deleterious
    effect on the gene or gene product (conservation,
    evolutionary, splicing impact, etc.)

    Please use the following columns to assign PM3
    if 2 or more of the following 3 predictors are disease causing:

    dbNSFP_MutationTaster_pred; "A" and "D" both count as disease causing.
    dbNSFP_Polyphen2_HVAR_pred; "D" and "P" both count as disease causing.
    dbNSFP_SIFT_pred; "D" count as disease causing.

    Assign PM3 if 2 or more of the following
    3 predictors are disease causing:
        - dbNSFP_phastCons46way_placental; >80% of the max
                value would be consider as disease causing.
        - dbNSFP_phyloP46way_placental; >80% of the max
                value be consider as disease causing.
        - dbNSFP_phyloP100way_vertebrate; >80% of the max
                value be consider as disease causing

    I think 1 is the max value for "dbNSFP_phastCons46way_placental"?
    so 80% of that is 0.8;
    Maybe 3 is the max value for "dbNSFP_phyloP46way_placental"?
    Maybe 10 is the max value for "dbNSFP_phyloP100way_vertebrate"?
    """
    counter_1 = []
    counter_2 = []
    max_value_dbNSFP_phastCons46way_placental = 1
    max_value_dbNSFP_phyloP46way_placental = 3
    max_value_dbNSFP_phyloP100way_vertebrate = 10

    if item["dbNSFP_MutationTaster_pred"] in ["A", "D"]:
        counter_1.append(True)
    else:
        counter_1.append(False)

    if item["dbNSFP_Polyphen2_HVAR_pred"] in ["D", "P"]:
        counter_1.append(True)
    else:
        counter_1.append(False)

    if (item["dbNSFP_SIFT_pred"] == "D"):
        counter_1.append(True)
    else:
        counter_1.append(False)

    try:
        if(float(item["dbNSFP_phastCons46way_placental"]) > max_value_dbNSFP_phastCons46way_placental * 0.8):
            counter_2.append(True)
        else:
            counter_2.append(False)

        if(float(item["dbNSFP_phyloP46way_placental"]) > max_value_dbNSFP_phyloP46way_placental * 0.8):
            counter_2.append(True)
        else:
            counter_2.append(False)

        if(float(item["dbNSFP_phyloP100way_vertebrate"]) > max_value_dbNSFP_phyloP100way_vertebrate * 0.8):
            counter_2.append(True)
        else:
            counter_2.append(False)

    except (ValueError, TypeError):
        return "TBD"

    if (sum(counter_1) >= 2 or sum(counter_2) >= 2):
        return True
    else:
        return False

def PP4(item):
    """
    Patient’s phenotype or family history is highly specific for
    a disease a single genetic etiology
    """
    pass


def PP5(item):
    """
    Reputable source recently reports variant as pathogenic, but
    the evidence is not available to the laboratory to
    perform an independent evaluation
    """
    pass


def BP1(item):
    """
    Missense variant in a gene for which primarily truncating
    variants are known to cause disease
    """
    pass


def BP2(item):
    """
    Observed in trans with a pathogenic variant for a fully
    penetrant dominant gene/disorder or observed in cis
    with a pathogenic variant in any inheritance pattern
    """
    pass


def BP3(item):
    """
    In-frame deletions/insertions in a repetitive region without a
    known function
    """
    pass


def BP4(item):
    """
    Multiple lines of computational evidence suggest no impact on gene or
    gene product (conservation, evolutionary, splicing impact, etc.)
    """
    pass


def BP5(item):
    """
    Variant found in a case with an alternate molecular basis
    for disease
    """
    pass


def BP6(item):
    """
    Reputable source recently reports variant as benign, but the evidence is
    not available to the laboratory to perform an independent evaluation
    """
    pass


def BP7(item):
    """
    A synonymous (silent) variant for which splicing prediction algorithms
    predict no impact to the splice consensus sequence nor the
    creation of a new splice site AND the nucleotide is not highly conserved
    """
    pass


def BS1(item):
    """
    Allele frequency is greater than expected
    for disorder
    """
    pass


def BS2(item):
    """
    Observed in a healthy adult individual for a recessive (homozygous),
    dominant (heterozygous), or X-linked (hemizygous) disorder, with
    full penetrance expected at an early age
    """
    pass


def BS3(item):
    """
    Well-established in vitro or in vivo functional studies show no
    damaging effect on protein function or splicing
    """
    pass


def BS4(item):
    """
    Lack of segregation in affected members of
    a family
    """
    pass


def BA1(item):
    """
    Allele frequency is >5% in Exome Sequencing Project, 1000 Genomes
    Project, or Exome Aggregation Consortium
    """
    pass


def Sequencing(item):
    """
    artifact as determined by depth, quality, or other previously
    reviewed data
    """
    pass
