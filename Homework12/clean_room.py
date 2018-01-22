import itertools
import numpy as np


class Game:
    def __init__(self):
        self.pool = self.gen_pool()
        self.unused = self.pool + []
        self.last_guess = None

    def start(self):
        game_mode = self.get_game_mode()

        if game_mode == 0:
            self.code_break()
        else:
            self.code_make()

    # ---------------- USER BREAKS CODE -------------------------------------------------------

    def code_make(self):
        code = self.generate_code()
        game_over = False

        while not game_over:
            guess = self.player_guess()
            game_over = self.compare(guess, code)

        print('gg ez')

    def get_game_mode(self):
        uinput = input('Select 0 to make a code or 1 to break a code')

        if uinput == '0':
            return 0
        elif uinput == '1':
            return 1

        return get_game_mode()

    def generate_code(self):
        colors = [1, 2, 3, 4, 5, 6]
        code = []

        while len(code) < 4:
            rnd_idx = randint(0, len(colors))
            code.append(colors[rnd_idx])
            colors.remove(colors[rnd_idx])

        return code

    def player_guess(self):
        user_input = input('Enter code or q to quit: ')

        if user_input.lower() == 'q':
            return None
        elif self.code_valid(user_input):
            return user_input
        else:
            return self.player_guess()

    def code_valid(self, code):
        allowed = [1, 2, 3, 4, 5, 6]

        if len(code) != 4:
            return False
        elif len(code) == len(set(code)):
            return False

        for c in code:
            if c not in allowed:
                return False

        return True

    def compare(self, guess, code):
        w_s = 0
        b_s = 0
        dots = 0

        for i in range(len(guess)):
            if guess[i] == code[i]:
                w_s += 1
            elif guess[i] in code:  # because unique chars in code and guess
                b_s += 1
            else:
                dots += 1

        print('Feedback: {}'.format(('w' * w_s) + ('b' * b_s) + ('.' * dots)))

        if w_s == 4:
            return True

        return False

    # ---------------- USER MAKES CODE -------------------------------------------------------

    def code_break(self):
        game_over = False
        feedback = ''
        print(
            'Make up your mind and select a 4 chars long code with number from 1 to 6 and no '
            'duplicates. Write it down somewhere. When feedback is requested from you, you should place' +
            'one w for each char that was in the right position, b for each char that is in your code but wrong '
            'position and for all other chars.')

        while not game_over:
            guess = self.ai_guess(feedback)

            if guess is None:
                print('Common, don\'t change your code in runtime, loser! Give me some feedback again!')

            feedback = self.get_user_feedback(guess)

            if feedback is None:
                print('gtfo loser!')

            game_over = feedback == 'wwww'

        print('gg ez')

    def get_user_feedback(self, guess):
        print("Is this your code: " + guess)
        response = input("Feedback pls: ")

        if self.validate_user_feedback(response):
            print("invalid response")
            self.get_user_feedback(guess)

        # format response
        chars = list(response)
        chars.sort(reverse=True)
        return "".join(chars)

    def validate_user_feedback(self, response, print_out=True):
        allowed = ['w', 'b', '.']

        if len(response) != 4:
            if print_out:
                print("Feedback not of length 4")
            return False
        elif len(response) - len(response.replace('.', '')) > 2:
            if print_out:
                print("No way to have more than 2 points")
            return False
        elif len(response) - len(response.replace('b', '')) == 1:
            if print_out:
                print("No way that only one character is not at its right position!")
            return False

        for c in response:
            if c not in allowed:
                if print_out:
                    print(str(c) + " is not an allowed character")
                return False

        return True

    def ai_guess(self, feedback):
        self.pool = self.eliminate_from_pool(feedback, self.last_guess)

        if len(self.pool) == 1:
            return self.pool[0]
        elif len(self.pool) == 0:
            return None

        scores = [self.get_score(x, self.pool) for x in self.unused]
        best_score = np.array(scores).argmax()

        result = self.unused[best_score]

        self.unused.remove(result)

        try:
            self.pool.remove(result)
        except:
            pass

        self.last_guess = result

        return result

    def eliminate_from_pool(self, feedback, guess):
        pool = self.pool + []

        if guess is None or feedback == '':
            return pool

        guess_set = set(guess)
        non_dots_count = len(feedback.replace('.', ''))
        b_count = len(feedback) - len(feedback.replace('b', ''))

        # remove all combinations that don't have exactly non_dots_count common elements
        pool = list(filter(lambda x: len(set(x).intersect(guess_set)) != non_dots_count, pool))

        # remove all permutations which are not possible due to the amount of b markers
        # maximum b_count - 1 characters in another position leads to an impossible combination
        # for example, b_count = 2, guess='1234', only combinations with 1 char not at right place removed,
        #                   so only '1234', as we can't swap just one char
        # 			   b_count = 3, guess = '1234', combos with max 2 char not at the same placed removed,
        #                   so '1234', '1243', '2134', ...
        # 			   b_count = 4, guess='1234', remove combinations with 3 chars not at the same place
        # 					Note: even if after the permutation, we now have 3 in their correct place, at least
        #                         1 is still wrong

        pool = list(filter(lambda x: set(x) == set(guess) and self.not_same_pos(x, guess) <= b_count - 1, pool))

        return pool

    def not_same_pos(self, x, y):
        different = 0

        for i in range(len(x)):
            if x[i] != y[i]:
                different += 1

        return different

    def get_score(self, x, pool):
        pool_len = len(pool)
        guess_combinations = [p for p in itertools.product("wb.", repeat=len(x))]
        possible_feedbacks = list(filter(lambda x: self.validate_user_feedback(x, print_out=False), guess_combinations))

        scores = [pool_len - len(eliminate_from_pool(feedback, x)) for feedback in possible_feedbacks]

        return min(scores)


if __name__ == "__main__":
    Game().start()
