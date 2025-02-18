from .mapping import mapping

def calculate_efficiency(rune):
    #calculate current and maximum rune efficiency

    #debugging
    #print("Mapping Data:", mapping)  
    #print("Main Stat Key:", rune["pri_eff"][0])  
    #print("Rune Class:", rune["class"])  
    #print("Type of mapping:", type(mapping))

    sub_ratio = 0.0
    pre_ratio = 0.0

    # Sub stat efficiency
    for stat in rune["sec_eff"]:
        stat_type = stat[0]
        stat_value = stat[1] + stat[3]  # Base value + bonus
        max_sub = mapping["rune"]["substat"][stat_type]["max"][6]
        sub_ratio += stat_value / max_sub

    # Prefix stat efficiency (innate stat)
    if rune.get("prefix_eff") and rune["prefix_eff"][0] > 0:
        prefix_stat = rune["prefix_eff"][0]
        prefix_value = rune["prefix_eff"][1]
        max_prefix = mapping["rune"]["substat"][prefix_stat]["max"][6]
        pre_ratio += prefix_value / max_prefix

    # Efficiency calculations
    current_efficiency = (sub_ratio*0.8 + pre_ratio*0.2)*70

    return {
        "rune_id": rune["rune_id"],
        "rune_set": rune["set_id"],
        "current_efficiency": round(current_efficiency, 2),
    }