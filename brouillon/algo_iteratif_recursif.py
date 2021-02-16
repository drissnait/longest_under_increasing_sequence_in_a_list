# encoding: utf-8

class LongSequenceIteratif:
    def plus_longue_sequence(self,liste):
        elements_to_process = []
        for i in range(len(liste)):
            elements_to_process.append([ListItem(liste[i], i)])
        longest_sequence = []
        while elements_to_process:
            element = elements_to_process.pop()
            for i in range(element[len(element) - 1].position + 1, len(liste)):
                for j in range(i, len(liste)):
                    if liste[j] > element[len(element) - 1].item:
                        elements_to_process.append(element + [ListItem(liste[j], j)])
                        if len(longest_sequence) < len(element) + 1:
                            longest_sequence = element + [ListItem(liste[j], j)]
        return list(map(lambda list_item: list_item.item, longest_sequence))


class LongSequenceRecurtif:

    def plus_longue_sequence(self, liste, depth=0, max_value=0):
        longest_sequence = [liste[0]]
        for i in range(len(liste)):
            for j in range(i + 1, len(liste)):
                if liste[j] > liste[i]:
                    if liste[j] > max_value:
                        sequence = [liste[i]] + self.plus_longue_sequence(liste[j: len(liste)], depth + 1, liste[i])
                        tmp = len(sequence) + depth + 1
                    if liste[j] <= max_value:
                        sequence = [liste[i]] + self.plus_longue_sequence(liste[j: len(liste)], 0, liste[i])
                        tmp = len(sequence)
                    if len(longest_sequence) < tmp:
                        longest_sequence = sequence
                    if len(longest_sequence) == tmp and sequence[0] > longest_sequence[0]:
                        longest_sequence = sequence
        return longest_sequence


class ListItem:
    def __init__(self, item, position):
        self.item = item
        self.position = position

    def __str__(self):
        return "[" + str(self.item) + "," + str(self.position) + "]"
        
        
liste=[10, 15, 7, 19, 2, 5, 7, 16, 3, 9, 15, 0, 1, 15, 6, 11, 0, 14, 7, 9]
l=LongSequenceIteratif()
print(l.plus_longue_sequence(liste))

