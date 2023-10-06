from Question import Question
import random

question_list = [
    Question("What covers most of Earth's surface?", "Clue: _ _ e _ _ _", "Oceans"),
    Question("What is the main gas in the Earth's atmosphere?", "Clue: _ _ y _ _ _", "Oxygen"),
    Question("What do fish use to breathe?", "Clue: _ i _ _ _ ", "Gills"),
    Question("What is a colorful underwater structure made of coral?", "Clue: _ _ e _", "Reef"),
    Question("What are tiny floating plants in the ocean?", "Clue: P _ y _ _ _ _ _ n k _ _ n ", "Phytoplankton"),
    Question("What do whales and dolphins use to communicate?", "Clue: E _ h _ _ _ c _ _ _ o n ", "Echolocation"),
    Question("What is the largest mammal in the ocean?", "Clue: _ _ a _ _", "Whale"),
    Question("What is the process of marine organisms sinking to the ocean floor?", "Clue: (2 words) Mar_ne  _ _ _ w ", "Marine snow"),
    Question("What is the study of marine life called?", "Clue: (2 words) M _ _ _ n _   _ i _ _ _ _ y ", "Marine biology"),
    Question("What are the strong ocean currents that flow underwater?", "Clue: T _ _ _ _ _ h _ _ _ n e", "Thermohaline"),
    Question("What is the zone where sunlight penetrates the ocean?", "Clue: S _ _ _ _ _ e", "Surface"),
    Question("What is the world's largest coral reef system?", "Clue: (3 words) Gre_t   Ba_rie_   _ _ _ f ", "Great Barrier Reef"),
    Question("What is the chemical that makes seawater salty?", "Clue: _ _ _ t ", "Salt"),
    Question("What is the transition zone between high and low tide called?", "Clue: I _ _ _ _ t _ _ _ l", "Intertidal"),
    Question("What is the process of species moving between habitats?", "Clue: _ _ _ r _ _ _ _ n ", "Migration")

]

def get_random_question():
    sentence = random.choice(question_list)
    return sentence
