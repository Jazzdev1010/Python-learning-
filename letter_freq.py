input_str = """The heart is a muscular organ found in humans and other animals. This organ pumps blood through the blood vessels.[1] The heart and blood vessels together make up the circulatory system.[2] The pumped blood carries oxygen and nutrients to the tissue, while carrying metabolic waste such as carbon dioxide to the lungs.[3] In humans, the heart is approximately the size of a closed fist and is located between the lungs, in the middle compartment of the chest, called the mediastinum.[4]

In humans, the heart is divided into four chambers: upper left and right atria and lower left and right ventricles.[5][6] Commonly, the right atrium and ventricle are referred together as the right heart and their left counterparts as the left heart.[7] In a healthy heart, blood flows one way through the heart due to heart valves, which prevent backflow.[4] The heart is enclosed in a protective sac, the pericardium, which also contains a small amount of fluid. The wall of the heart is made up of three layers: epicardium, myocardium, and endocardium.[8]

The heart pumps blood with a rhythm determined by a group of pacemaker cells in the sinoatrial node. These generate an electric current that causes the heart to contract, traveling through the atrioventricular node and along the conduction system of the heart. In humans, deoxygenated blood enters the heart through the right atrium from the superior and inferior venae cavae and passes to the right ventricle. From here, it is pumped into pulmonary circulation to the lungs, where it receives oxygen and gives off carbon dioxide. Oxygenated blood then returns to the left atrium, passes through the left ventricle and is pumped out through the aorta into systemic circulation, traveling through arteries, arterioles, and capillaries—where nutrients and other substances are exchanged between blood vessels and cells, losing oxygen and gaining carbon dioxide—before being returned to the heart through venules and veins.[9] The adult heart beats at a resting rate close to 72 beats per minute.[10]
"""
stopwords = [
    'a', 'all', 'along', 'also', 'an', 'and', 'are', 'as', 'at', 'be', 
    'before', 'between', 'by', 'due', 'from', 'further', 'has', 'in', 
    'into', 'is', 'it', 'its', 'of', 'off', 'on', 'once', 'other', 
    'out', 'the', 'their', 'these', 'this', 'through', 'to', 'upper', 
    'was', 'where', 'while', 'which', 'with'
]

def remove_stopwords(text,stopwords):
    """_summary_

    Args:
        text (str): Input bulk string
        stopwords (list): List of stop words

    Returns:
        list: words without stopwords
    """
    words = []
    for word in text.split():
        if word.lower() not in stopwords:
            words.append(clean_word(word))
    return words
             

for word in input_str.split():
    if word.endswith(']'):
        print(word)
        print(word[:-4])
        print(word.split('.')[0])
        parts = word.split('.')
        print(parts)
        print(parts[0])
        print(parts[-1])
        
def clean_word(word_str):
    """_summary_

    Args:
       Input: word_str (str): 'minute.[10]'

    Returns:
       Output(str): minute
    """
    return word_str.split('.')[0]
    

def count_freq(word_list):
    freq = {}
    for word in word_list:
        if word in list(freq.keys()):
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


def top(word_freq):
    largest_num = 0
    word = ""
    for key,value in word_freq.items():
        if value > largest_num:
            largest_num = value
            word = key
    return {word:largest_num}

words_without_stopwords = remove_stopwords(input_str, stopwords)
print(top(count_freq(words_without_stopwords)))





