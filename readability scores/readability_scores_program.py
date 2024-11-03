from user_input import user_input
from results_text_analysis import print_text_statistics, print_readability_scores

texte = user_input()
print_text_statistics(texte)
print_readability_scores(texte)
