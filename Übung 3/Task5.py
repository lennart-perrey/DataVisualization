prob_protanopia = 0.0245
prob_deuteranopia = 0.061
prob_tritanopia = 0.00011

prob_none_colorblind = (1 - prob_protanopia) * (1 - prob_deuteranopia) * (1 - prob_tritanopia)
prob_at_least_one_colorblind = 1 - prob_none_colorblind

print(f"The probability that at least one male reviewer is color blind: {prob_at_least_one_colorblind:.4%}")