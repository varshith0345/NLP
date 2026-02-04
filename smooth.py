word_counts={'apple':5,'banana':2,'cherry':0}
vocabulory=10
total=sum(word_counts.values())
def calculate_laplace(word):
    count=word_counts.get(word,0)
    probability=(count+1)/(total+vocabulory)
    return probability
new_word='cherry'
result=calculate_laplace(new_word)
print(result)