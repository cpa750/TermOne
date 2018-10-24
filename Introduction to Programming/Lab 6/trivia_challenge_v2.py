import pickle, shelve

import trivia_challenge

questions = trivia_challenge.read_questions()
points = trivia_challenge.main(questions)


