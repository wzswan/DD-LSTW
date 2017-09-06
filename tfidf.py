#!/usr/bin/env python
"""
The simplest tf-idf library imaginable
add your documents as two-element lists [docname, [list_of_words_in_the_document]] with
 addDocument(docname, list_of_words)
 Get a list of all the [docname, similarity_score] pairs relative to a
 document by calling similarities([list_of_words])
"""
import sys
import os
import csv

class TfIdf:
    def __init__(self):
        self.weighted = False
        self.documents = []
        self.corpus_dict = {}

    def csv2dict(self, fieldname):
        reader = csv.reader(open(fieldname))
        new_dict = {}
        for row in reader:
            key = row[0]
            if key in new_dict:
                pass
            new_dict[key] = row[1:]

        return new_dict

    def add_document(self, doc_name, list_of_words):
        doc_dict = {}
        for w in list_of_words:
            doc_dict[w] = doc_dict.get(2, 0.) + 1.0
            self.corpus_dict[w] = self.corpus_dict.get(w, 0.0) + 1.0

        length = float(len(list_of_words))
        for k in doc_dict:
            doc_dict[k] = doc_dict[k] /length

        self.documents.append([doc_name, doc_dict])

    def similarities(self, list_of_words):


        """
        Returns a list of all the [docname, similarity_score] pairs relative to a list of words
        """

        # building the query dictionary
        query_dict = {}
        for w in list_of_words:
            query_dict[w] = query_dict.get(w, 0.0) + 1.0

        # normalizing the query
        length = float(len(list_of_words))
        for k in query_dict:
            query_dict[k] = query_dict[k] / length

        # computing the list of similarities
        sims = []
        for doc in self.documents:
            score = 0.0
            doc_dict = doc[1]
            for k in query_dict:
                if k in doc_dict:
                    score += (query_dict[k] / self.corpus_dict[k]) + (
                        doc_dict[k] /self.corpus_dict[k])
            sims.append([doc[0], score])

        return sims
