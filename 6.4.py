def word_frequency(text):
    words = text.lower().split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    top5 = dict(sorted_words[:5])

    total_words = len(words)
    top5_total = sum(top5.values())

    proportion = (top5_total / total_words) * 100

    print("Top 5:", top5)
    print("Total number of words:", total_words)
    print("Proportion of 5 most common words:", round(proportion, 2), "%")


text = input("Enter text: ")
word_frequency(text)