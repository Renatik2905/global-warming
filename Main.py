import pygame
import random

pygame.init()

# Window settings
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1040
WHITE = (127, 53, 255)
BLACK = (230, 213, 101)
FONT = pygame.font.Font(None, 36)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Вопросы про Глобальнео потепление(Что-то на подобе диктанта по биологии) ОТВЕЧАЙТЕ АНГЛ. БУКВАМИ")

questions = [
    {
        "question": "1.Какое из перечисленных явлений не является последствием глобального потепления?",
        "options": ["A. Разрушение озонового слоя", "B. Поднятие уровня мирового океана", "C. Увеличение числа природных катастроф", "D. Незнаю"],
        "correct_answer": "A"
    },
    {
        "question": "2.Какой газ является основным парниковым газом, усиливающим глобальное потепление?",
        "options": ["A. Кислород", "B. Диоксид азота", "C. Диоксид углерода", "D. Незнаю"],
        "correct_answer": "C"
    },
    {
        "question": "4.Как называется явление, при котором температура Земли увеличивается за счет удержания тепла в атмосфере?",
        "options": ["A. Глобальное охлаждение", "B.Глобальное потепление", "C. Климатический кризис", "D. Незнаю"],
        "correct_answer": "B"
    },
    {
        "question": "5.Какое количество углекислого газа человечество пускает в атмосферу ежегодно из-за деятельности человека?",
        "options": ["A. 10 миллиардов тонн", "B. 15 миллиардов тонн", "C. 20 миллиардов тонн", "D. 25 миллиардов тонн"],
        "correct_answer": "C"
    },
    {
        "question": "6.Какая часть Земли страдает от глобального потепления наиболее сильно?",
        "options": ["A. Экваториальная зона", "B. Арктика", "C. Экватор", "D. Незнаю"],
        "correct_answer": "B"
    },
    {
        "question": "7.Какое действие может помочь снизить уровень глобального потепления?",
        "options": ["A. Увеличение использования ископаемых топлив", "B. Осуществление энергосберегающих мероприятий", "C. Увеличение сжигания мусора", "D. Незнаю"],
        "correct_answer": "B"
    },
    {
        "question": "8.Как можно организовать защиту от негативных последствий глобального потепления?",
        "options": ["A. Увеличить вырубку лесов", "B. Развивать экологически чистые источники энергии", "C. Увеличить количество выбросов загрязняющих веществ", "D. Незнаю"],
        "correct_answer": "B"
    },
    {
        "question": "9.Какой прогнозируемый эффект связан с глобальным потеплением?",
        "options": ["A. Увеличение засух и пустынь", "B. Снижение уровня моря", "C.Уменьшение площади лесов", "D. Незнаю"],
        "correct_answer": "A"
    },
    {
        "question": "10.Вы хотите боротся с Глобальным потеплением?",
        "options": ["A. Да", "B. Нет", "C. No","D. Незнаю"],
        "correct_answer": "A"
    },
   
]   

current_question = 0
score = 0

def display_question(question):
    window.fill(WHITE)
    
    text = FONT.render(question["question"], True, BLACK)
    text_rect = text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 50))
    window.blit(text, text_rect)
    
    options_y = WINDOW_HEIGHT//2
    for option in question["options"]:
        option_text = FONT.render(option, True, BLACK)
        option_rect = option_text.get_rect(center=(WINDOW_WIDTH//2, options_y))
        window.blit(option_text, option_rect)
        options_y += 50

def display_result(score):
    window.fill(WHITE)
    
    text = FONT.render(f"Ваш счет:) : {score}", True, BLACK)
    text_rect = text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
    window.blit(text, text_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key = event.unicode.upper()
            if key == "A" or key == "B" or key == "C" or key == "D":
                if key == questions[current_question]["correct_answer"]:
                    score += 1
                current_question += 1
                if current_question == len(questions):
                    display_result(score)
                else:
                    display_question(questions[current_question])

    if current_question < len(questions):
        display_question(questions[current_question])

    pygame.display.update()

pygame.quit()
