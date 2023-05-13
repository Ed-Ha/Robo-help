
from flask import Flask, render_template, request, jsonify, redirect, url_for
from api_req import handle_API_request





car_mechanic_start_line = "Hello! I'm Car Mechanic Robot.\nAsk me anything about your car."
doctor_start_line = "Hello! I'm Doctor Robot.\nAsk me for medical advice and diagnosis."
stock_market_trader_start_line = "Hello! I'm Stock Market Trader Robot.\nAsk me for insights on the stock market."
nutritionist_start_line = "Hello! I'm Nutritionist Robot.\nAsk me for advice on healthy eating."
personal_trainer_start_line = "Hello! I'm Personal Trainer Robot.\nAsk me for workout advice."
software_developer_start_line = "Hello! I'm Software Developer Robot.\nAsk me for help with your code."
career_counselor_start_line = "Hello! I'm Career Counselor Robot.\nAsk me for advice on your career path."
marriage_counselor_start_line = "Hello! I'm Marriage Counselor Robot.\nAsk me for advice on your marriage or relationship."
financial_planner_start_line = "Hello! I'm Financial Planner Robot.\nAsk me for advice on managing your finances."
dog_trainer_start_line = "Hello! I'm Dog Trainer Robot.\nAsk me for advice on training your dog."
travel_agent_start_line = "Hello! I'm Travel Agent Robot.\nAsk me for advice on planning your next trip."
graphic_designer_start_line = "Hello! I'm Graphic Designer Robot.\nAsk me for help with your design projects."
real_estate_agent_start_line = "Hello! I'm Real Estate Agent Robot.\nAsk me for advice on buying or selling a property."
chef_start_line = "Hello! I'm Chef Robot.\nAsk me for cooking advice or recipe ideas."
architect_start_line = "Hello! I'm Architect Robot.\nAsk me for advice on your architectural projects."
fashion_stylist_start_line = "Hello! I'm Fashion Stylist Robot.\nAsk me for advice on your wardrobe and fashion style."
marketing_consultant_start_line = "Hello! I'm Marketing Consultant Robot.\nAsk me for advice on your marketing strategy."
horticulturist_start_line = "Hello! I'm Horticulturist Robot.\nAsk me for advice on gardening and plant care."

car_mechanic_start_line_he = "אהלן! אני מר רובוט ואני מוסכניק. שאל אותי כל שאלה בקשר לרכב שלך."
doctor_start_line_he = "שלום! אני דוקטור רובוט.\nשאל אותי שאלות לגבי טיפולים ואבחנות רפואיות."
stock_market_trader_start_line_he = "אהלן! אני מר רובוט ואני יועץ השקעות. שאל אותי שאלות לגבי שוק ההון והשקעות."
nutritionist_start_line_he = "שלום! אני מר רובוט ואני תזונאי. שאל אותי שאלות ובקש עצות לשמירה על תזונה נכונה ובריאה."
personal_trainer_start_line_he = "שלום! אני מר רובוט ואני מאמן כושר. שאל אותי שאלות בקשר לאימונים, פיתוח גוף וכושר."
software_developer_start_line_he = "אהלן! אני מר רובוט ואני מפתח תוכנה. שאל אותי כל שאלה בקשר לקוד שלך ואעזור בשמחה."
career_counselor_start_line_he = "שלום! אני מר רובוט ואני יועץ תעסוקה. אני כאן כדי לייעץ לך בנושא קריירה ותעסוקה."
marriage_counselor_start_line_he = "שלום! אני מר רובוט ואני יועץ תעסוקה. אני כאן כדי לייעץ לך בנושא קריירה ותעסוקה."
financial_planner_start_line_he = "שלום! אני מר רובוט ואני יועץ כלכלי. שאל אותי וקבל עצות לגבי ניהול הכספים שלך."
dog_trainer_start_line_he = "שלום! אני מר רובוט ואני מאלף כלבים. שאל אותי כל שאלה בנוגע לאילוף הכלב שלך."
travel_agent_start_line_he = "שלום! אני מר רובוט ואני סוכן נסיעות. שאל אותי לגבי טיפים, מסלולים ותכנון הטיול הבא שלך."
graphic_designer_start_line_he = "שלום! אני מר רובוט ואני מעצב גרפי. שאל אותי כל שאלה לגבי פרוייקטים ועיצוב גרפי."
real_estate_agent_start_line_he = "שלום! אני מר רובוט ואני סוכן נדלן. שאל אותי כל שאלה לגבי קנייה או מכירה של נכסים."
chef_start_line_he = "שלום! אני מר רובוט ואני שף. שאל אותי שאלות לגבי בישול ובקש מתכונים"
architect_start_line_he = "שלום! אני מר רובוט ואני אדריכל.\nשאל אותי וקבל עצות לגבי פרוייקט האדריכלות שלך."
fashion_stylist_start_line_he = "שלום! אני מר רובוט ואני סטייליסט. שאל אותי כל דבר לגבי פרטי לבוש ואופנה."
marketing_consultant_start_line_he = "שלום, אני מר רובוט ואני יועץ שיווקי. שאל אותי שאלות לגבי אסטרטגיות שיווק."
horticulturist_start_line_he = "שלום, אני מר רובוט ואני גנן! שאל אותי שאלות לגבי גינון, צמחים וטיפוח הגינה."

en_category_cards = {
    'Car_Mechanic': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Car_Mechanic"><img src="/../static/images/Car_Mechanic.jpeg" alt="Car Mechanic" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Car Mechanic</h2>
<p class="mb-0">{car_mechanic_start_line}</p>
''',
    'Doctor': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Doctor"><img src="/../static/images/Doctor.jpeg" alt="Doctor" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Doctor</h2>
<p class="mb-0">{doctor_start_line}</p>
''',
    'Stock_Market_Trader': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Stock_Market_Trader"><img src="/../static/images/Stock_Market_Trader.jpeg" alt="Stock Market Trader" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Stock Market Trader</h2>
<p class="mb-0">{stock_market_trader_start_line}</p>
''',
    'Nutritionist': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Nutritionist"><img src="/../static/images/Nutritionist.jpeg" alt="Nutritionist" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Nutritionist</h2>
<p class="mb-0">{nutritionist_start_line}</p>
''',
    'Personal_Trainer': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Personal_Trainer"><img src="/../static/images/Personal_Trainer.jpeg" alt="Personal Trainer" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Personal Trainer</h2>
<p class="mb-0">{personal_trainer_start_line}</p>
''',
    'Software_Developer': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Software_Developer"><img src="/../static/images/Software_Developer.jpeg" alt="Software Developer" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Software Developer</h2>
<p class="mb-0">{software_developer_start_line}</p>
''',
    'Career_Counselor': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Career_Counselor"><img src="/../static/images/Career_Counselor.jpeg" alt="Career Counselor" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Career Counselor</h2>
<p class="mb-0">{career_counselor_start_line}</p>
''',
    'Marriage_Counselor': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Marriage_Counselor"><img src="/../static/images/Marriage_Counselor.jpeg" alt="Marriage Counselor" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Marriage Counselor</h2>
<p class="mb-0">{marriage_counselor_start_line}</p>
''',
    'Financial_Planner': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Financial_Planner"><img src="/../static/images/Financial_Planner.jpeg" alt="Financial Planner" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Financial Planner</h2>
<p class="mb-0">{financial_planner_start_line}</p>
''',
    'Dog_Trainer': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Dog_Trainer"><img src="/../static/images/Dog_Trainer.jpeg" alt="Dog Trainer" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Dog Trainer</h2>
<p class="mb-0">{dog_trainer_start_line}</p>
''',
    'Travel_Agent': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Travel_Agent"><img src="/../static/images/Travel_Agent.jpeg" alt="Travel Agent" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Travel Agent</h2>
<p class="mb-0">{travel_agent_start_line}</p>
''',
    'Graphic_Designer': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Graphic_Designer"><img src="/../static/images/Graphic_Designer.jpeg" alt="Graphic Designer" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Graphic Designer</h2>
<p class="mb-0">{graphic_designer_start_line}</p>
''',
    'Real_Estate_Agent': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Real_Estate_Agent"><img src="/../static/images/Real_Estate_Agent.jpeg" alt="Real Estate Agent" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Real Estate Agent</h2>
<p class="mb-0">{real_estate_agent_start_line}</p>
''',
    'Chef': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Chef"><img src="/../static/images/Chef.jpeg" alt="Chef" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Chef</h2>
<p class="mb-0">{chef_start_line}</p>
''',
    'Architect': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Architect"><img src="/../static/images/Architect.jpeg" alt="Architect" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Architect</h2>
<p class="mb-0">{architect_start_line}</p>
''',
    'Fashion_Stylist': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Fashion_Stylist"><img src="/../static/images/Fashion_Stylist.jpeg" alt="Fashion Stylist" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Fashion Stylist</h2>
<p class="mb-0">{fashion_stylist_start_line}</p>
''',
    'Marketing_Consultant': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Marketing_Consultant"><img src="/../static/images/Marketing_Consultant.jpeg" alt="Marketing Consultant" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Marketing Consultant</h2>
<p class="mb-0">{marketing_consultant_start_line}</p>
''',
    'Horticulturist': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Horticulturist"><img src="/../static/images/Horticulturist.jpeg" alt="Horticulturist" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">Horticulturist</h2>
<p class="mb-0">{horticulturist_start_line}</p>'''
}

heb_category_cards = {
    'מוסכניק': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Car_Mechanic"><img src="/../static/images/Car_Mechanic.jpeg" alt="Car Mechanic" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">מוסכניק</h2>
<p class="mb-0">{car_mechanic_start_line_he}</p>
''',
    'רופא': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Doctor"><img src="/../static/images/Doctor.jpeg" alt="Doctor" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">רופא</h2>
<p class="mb-0">{doctor_start_line_he}</p>
''',
    'יועץ השקעות': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Stock_Market_Trader"><img src="/../static/images/Stock_Market_Trader.jpeg" alt="Stock Market Trader" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">יועץ השקעות</h2>
<p class="mb-0">{stock_market_trader_start_line_he}</p>
''',
    'תזונאי': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Nutritionist"><img src="/../static/images/Nutritionist.jpeg" alt="Nutritionist" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">תזונאי</h2>
<p class="mb-0">{nutritionist_start_line_he}</p>
''',
    'מאמן כושר': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Personal_Trainer"><img src="/../static/images/Personal_Trainer.jpeg" alt="Personal Trainer" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">מאמן כושר</h2>
<p class="mb-0">{personal_trainer_start_line_he}</p>
''',
    'מפתח תוכנה': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Software_Developer"><img src="/../static/images/Software_Developer.jpeg" alt="Software Developer" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">מפתח תוכנה</h2>
<p class="mb-0">{software_developer_start_line_he}</p>
''',
    'יועץ קריירה': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Career_Counselor"><img src="/../static/images/Career_Counselor.jpeg" alt="Career Counselor" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">יועץ קריירה</h2>
<p class="mb-0">{career_counselor_start_line_he}</p>
''',
    'יועץ נישואים': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Marriage_Counselor"><img src="/../static/images/Marriage_Counselor.jpeg" alt="Marriage Counselor" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">יועץ נישואים</h2>
<p class="mb-0">{marriage_counselor_start_line_he}</p>
''',
    'יועץ כלכלי': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Financial_Planner"><img src="/../static/images/Financial_Planner.jpeg" alt="Financial Planner" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">יועץ כלכלי</h2>
<p class="mb-0">{financial_planner_start_line_he}</p>
''',
    'מאלף כלבים': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Dog_Trainer"><img src="/../static/images/Dog_Trainer.jpeg" alt="Dog Trainer" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">מאלף כלבים</h2>
<p class="mb-0">{dog_trainer_start_line_he}</p>
''',
    'סוכן נסיעות': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Travel_Agent"><img src="/../static/images/Travel_Agent.jpeg" alt="Travel Agent" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">סוכן נסיעות</h2>
<p class="mb-0">{travel_agent_start_line_he}</p>
''',
    'מעצב גרפי': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Graphic_Designer"><img src="/../static/images/Graphic_Designer.jpeg" alt="Graphic Designer" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">מעצב גרפי</h2>
<p class="mb-0">{graphic_designer_start_line_he}</p>
''',
    'סוכן נדל\"ן': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Real_Estate_Agent"><img src="/../static/images/Real_Estate_Agent.jpeg" alt="Real Estate Agent" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">סוכן נדל"ן</h2>
<p class="mb-0">{real_estate_agent_start_line_he}</p>
''',
    'שף': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Chef"><img src="/../static/images/Chef.jpeg" alt="Chef" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">שף</h2>
<p class="mb-0">{chef_start_line_he}</p>
''',
    'אדריכל': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Architect"><img src="/../static/images/Architect.jpeg" alt="Architect" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">אדריכל</h2>
<p class="mb-0">{architect_start_line_he}</p>
''',
    'סטייליסט': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Fashion_Stylist"><img src="/../static/images/Fashion_Stylist.jpeg" alt="Fashion Stylist" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">סטייליסט</h2>
<p class="mb-0">{fashion_stylist_start_line_he}</p>
''',
    'יועץ שיווק': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Marketing_Consultant"><img src="/../static/images/Marketing_Consultant.jpeg" alt="Marketing Consultant" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">יועץ שיווק</h2>
<p class="mb-0">{marketing_consultant_start_line_he}</p>
''',
    'גנן': f'''<div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><a href="Horticulturist"><img src="/../static/images/Horticulturist.jpeg" alt="Horticulturist" width="100px" height="100px" ></a></div>
<h2 class="fs-4 fw-bold">גנן</h2>
<p class="mb-0">{horticulturist_start_line_he}</p>'''
}

en_categories = ['Doctor', 'Car_Mechanic', 'Stock_Market_Trader', 'Nutritionist', 'Personal_Trainer',
                 'Software_Developer', 'Career_Counselor', 'Marriage_Counselor', 'Financial_Planner', 'Dog_Trainer',
                 'Travel_Agent', 'Graphic_Designer', 'Real_Estate_Agent', 'Chef', 'Architect', 'Fashion_Stylist',
                 'Marketing_Consultant', 'Horticulturist']
heb_categories = ['רופא', 'מוסכניק', 'יועץ השקעות', 'תזונאי', 'מאמן כושר', 'מפתח תוכנה', 'יועץ קריירה', 'יועץ נישואים',
                  'יועץ כלכלי', 'מאלף כלבים', 'סוכן נסיעות', 'מעצב גרפי', 'סוכן נדל\"ן', 'שף', 'אדריכל', 'סטייליסט',
                  'יועץ שיווק', 'גנן']

doctor_start_prompt = {"role": "user",
                       "content": "I have a medical issue, during our current conversation you will answer as a "
                                  "Doctor. make sure to give responsible answers and ask questions in order to focus "
                                  "your answer. write your answer in hebrew.\nlet's start:\n "
                       }
car_mechanic_start_prompt = {"role": "user",
                             "content": "I have an issue with my car, during our current conversation you will answer "
                                        "as a Car Mechanic. Please make sure to give responsible answers and ask "
                                        "questions in order to focus your answer. Let's start:\n "
                             }

stock_market_trader_start_prompt = {"role": "user",
                                    "content": "I want to know more about the stock market, during our current "
                                               "conversation you will answer as a Stock Market Trader. Please make "
                                               "sure to give responsible answers and ask questions in order to focus "
                                               "your answer. Let's start:\n "
                                    }

nutritionist_start_prompt = {"role": "user",
                             "content": "I want to improve my eating habits, during our current conversation you will "
                                        "answer as a Nutritionist. Please make sure to give responsible answers and "
                                        "ask questions in order to focus your answer. Let's start:\n "
                             }

personal_trainer_start_prompt = {"role": "user",
                                 "content": "I want to start a workout routine, during our current conversation you "
                                            "will answer as a Personal Trainer. Please make sure to give responsible "
                                            "answers and ask questions in order to focus your answer. Let's start:\n "
                                 }

software_developer_start_prompt = {"role": "user",
                                   "content": "I need help with my code, during our current conversation you will "
                                              "answer as a Software Developer. Please make sure to give responsible "
                                              "answers and ask questions in order to focus your answer. Let's start:\n "
                                   }

career_counselor_start_prompt = {"role": "user",
                                 "content": "I need advice on my career path, during our current conversation you "
                                            "will answer as a Career Counselor. Please make sure to give responsible "
                                            "answers and ask questions in order to focus your answer. Let's start:\n "
                                 }

marriage_counselor_start_prompt = {"role": "user",
                                   "content": "I need advice on my marriage/relationship, during our current "
                                              "conversation you will answer as a Marriage Counselor. Please make sure "
                                              "to give responsible answers and ask questions in order to focus your "
                                              "answer. Let's start:\n "
                                   }

financial_planner_start_prompt = {"role": "user",
                                  "content": "I need help managing my finances, during our current conversation you "
                                             "will answer as a Financial Planner. Please make sure to give "
                                             "responsible answers and ask questions in order to focus your answer. "
                                             "Let's start:\n "
                                  }

dog_trainer_start_prompt = {"role": "user",
                            "content": "I need advice on training my dog, during our current conversation you will "
                                       "answer as a Dog Trainer. Please make sure to give responsible answers and ask "
                                       "questions in order to focus your answer. Let's start:\n "
                            }

travel_agent_start_prompt = {"role": "user",
                             "content": "I need help planning my next trip, during our current conversation you will "
                                        "answer as a Travel Agent. Please make sure to give responsible answers and "
                                        "ask questions in order to focus your answer. Let's start:\n "
                             }

graphic_designer_start_prompt = {"role": "user",
                                 "content": "I need help with my design project, during our current conversation you "
                                            "will answer as a Graphic Designer. Please make sure to give responsible "
                                            "answers and ask questions in order to focus your answer. Let's start:\n "
                                 }

real_estate_agent_start_prompt = {"role": "user",
                                  "content": "I need advice on buying or selling a property, during our current "
                                             "conversation you will answer as a Real Estate Agent. Please make sure "
                                             "to give responsible answers and ask questions in order to focus your "
                                             "answer. Let's start:\n "
                                  }

chef_start_prompt = {"role": "user",
                     "content": "I need cooking advice or recipe ideas, during our current conversation you will "
                                "answer as a Chef. Please make sure to give responsible answers and ask questions in "
                                "order to focus your answer. Let's start:\n "
                     }

architect_start_prompt = {"role": "user",
                          "content": "I need advice on my architectural project, during our current conversation you "
                                     "will answer as an Architect. Please make sure to give responsible answers and "
                                     "ask questions in order to focus your answer. Let's start:\n "
                          }

fashion_stylist_start_prompt = {"role": "user",
                                "content": "I need advice on my wardrobe and fashion style, during our current "
                                           "conversation you will answer as a Fashion Stylist. Please make sure to "
                                           "give responsible answers and ask questions in order to focus your answer. "
                                           "Let's start:\n "
                                }

marketing_consultant_start_prompt = {"role": "user",
                                     "content": "I need advice on my marketing strategy, during our current "
                                                "conversation you will answer as a Marketing Consultant. Please make "
                                                "sure to give responsible answers and ask questions in order to focus "
                                                "your answer. Let's start:\n "
                                     }

horticulturist_start_prompt = {"role": "user",
                               "content": "I need advice on gardening and plant care, during our current conversation "
                                          "you will answer as a Horticulturist. Please make sure to give responsible "
                                          "answers and ask questions in order to focus your answer. Let's start:\n "
                               }

professions = {
    'Doctor': {'he start line': doctor_start_line_he, 'start line': doctor_start_line,
               'start prompt': doctor_start_prompt, 'messages': [doctor_start_prompt]},
    'Car_Mechanic': {'he start line': car_mechanic_start_line_he, 'start line': car_mechanic_start_line,
                     'start prompt': car_mechanic_start_prompt, 'messages': [car_mechanic_start_prompt]},
    'Stock_Market_Trader': {'he start line': stock_market_trader_start_line_he,
                            'start line': stock_market_trader_start_line,
                            'start prompt': stock_market_trader_start_prompt,
                            'messages': [stock_market_trader_start_prompt]},
    'Nutritionist': {'he start line': nutritionist_start_line_he, 'start line': nutritionist_start_line,
                     'start prompt': nutritionist_start_prompt, 'messages': [nutritionist_start_prompt]},
    'Personal_Trainer': {'he start line': personal_trainer_start_line_he, 'start line': personal_trainer_start_line,
                         'start prompt': personal_trainer_start_prompt, 'messages': [personal_trainer_start_prompt]},
    'Software_Developer': {'he start line': software_developer_start_line_he,
                           'start line': software_developer_start_line, 'start prompt': software_developer_start_prompt,
                           'messages': [software_developer_start_prompt]},
    'Career_Counselor': {'he start line': career_counselor_start_line_he, 'start line': career_counselor_start_line,
                         'start prompt': career_counselor_start_prompt, 'messages': [career_counselor_start_prompt]},
    'Marriage_Counselor': {'he start line': marriage_counselor_start_line_he,
                           'start line': marriage_counselor_start_line, 'start prompt': marriage_counselor_start_prompt,
                           'messages': [marriage_counselor_start_prompt]},
    'Financial_Planner': {'he start line': financial_planner_start_line_he, 'start line': financial_planner_start_line,
                          'start prompt': financial_planner_start_prompt, 'messages': [financial_planner_start_prompt]},
    'Dog_Trainer': {'he start line': dog_trainer_start_line_he, 'start line': dog_trainer_start_line,
                    'start prompt': dog_trainer_start_prompt, 'messages': [dog_trainer_start_prompt]},
    'Travel_Agent': {'he start line': travel_agent_start_line_he, 'start line': travel_agent_start_line,
                     'start prompt': travel_agent_start_prompt, 'messages': [travel_agent_start_prompt]},
    'Graphic_Designer': {'he start line': graphic_designer_start_line_he, 'start line': graphic_designer_start_line,
                         'start prompt': graphic_designer_start_prompt, 'messages': [graphic_designer_start_prompt]},
    'Real_Estate_Agent': {'he start line': real_estate_agent_start_line_he, 'start line': real_estate_agent_start_line,
                          'start prompt': real_estate_agent_start_prompt, 'messages': [real_estate_agent_start_prompt]},
    'Chef': {'he start line': chef_start_line_he, 'start line': chef_start_line, 'start prompt': chef_start_prompt,
             'messages': [chef_start_prompt]},
    'Architect': {'he start line': architect_start_line_he, 'start line': architect_start_line,
                  'start prompt': architect_start_prompt, 'messages': [architect_start_prompt]},
    'Fashion_Stylist': {'he start line': fashion_stylist_start_line_he, 'start line': fashion_stylist_start_line,
                        'start prompt': fashion_stylist_start_prompt, 'messages': [fashion_stylist_start_prompt]},
    'Marketing_Consultant': {'he start line': marketing_consultant_start_line_he,
                             'start line': marketing_consultant_start_line,
                             'start prompt': marketing_consultant_start_prompt,
                             'messages': [marketing_consultant_start_prompt]},
    'Horticulturist': {'he start line': horticulturist_start_line_he, 'start line': horticulturist_start_line,
                       'start prompt': horticulturist_start_prompt, 'messages': [horticulturist_start_prompt]}
}



def start_chat(profession, lang="en"):
    global professions

    display_messages = []

    if request.method == 'GET':
        display_messages = professions[profession]['messages']
        display_messages[0].update({"role": "assistant"})

        #handle language
        if lang == "heb":
            display_messages[0].update({"content": professions[profession]['he start line']})
            return render_template(f'{profession}_heb.html', messages=display_messages)
        else:
            display_messages[0].update({"content": professions[profession]['start line']})
            return render_template(f'{profession}.html', messages=display_messages)


    elif request.method == 'POST':
        message = request.form['message']
        professions[profession]['messages'].append({"role": "user", "content": message})
        professions[profession]['messages'] = handle_API_request(professions[profession]['messages'])
        display_messages = professions[profession]['messages']
        display_messages[0].update({"role": "assistant"})
        # handle language
        if lang == "heb":
            display_messages[0].update({"content": professions[profession]['he start line']})
            return render_template(f'{profession}_heb.html', messages=display_messages)
        else:
            display_messages[0].update({"content": professions[profession]['start line']})
            return render_template(f'{profession}.html', messages=display_messages)

    else:
        print("error! request is not get or post")



def clear_history():
    global professions
    for profession in professions:
        professions[profession]['messages'].clear()
        professions[profession]['messages'].append(professions[profession]['start prompt'])




app = Flask(__name__)




@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    filtered_html = ''
    filtered_categories_heb = [category for category in heb_categories if query in category]
    filtered_categories = [category for category in en_categories if query in category.lower()]

    for category in filtered_categories:
        filtered_html += f'<div class="col-lg-6 col-xxl-4 mb-5" data-category="{category}">' + f''' <div class="card bg-light border-0 h-100">
                                <div class="card-body text-center p-4 p-lg-5 pt-0 pt-lg-0">''' + en_category_cards[
            category] + '''</div></div></div>'''
    for category in filtered_categories_heb:
        filtered_html += f'<div class="col-lg-6 col-xxl-4 mb-5" data-category="{category}">' + f''' <div class="card bg-light border-0 h-100">
                            <div class="card-body text-center p-4 p-lg-5 pt-0 pt-lg-0">''' + heb_category_cards[
            category] + '''</div></div></div>'''

    return jsonify({'html': f'<div class="row gx-lg-5">{filtered_html}</div>'})




@app.route('/heb/search')
def search_heb():
    query = request.args.get('query', '').lower()
    filtered_categories = [category for category in en_categories if query in category.lower()]
    filtered_html = ''
    for category in filtered_categories:
        filtered_html += f'<div class="col-lg-6 col-xxl-4 mb-5" data-category="{category}">' + f''' <div class="card bg-light border-0 h-100">
                            <div class="card-body text-center p-4 p-lg-5 pt-0 pt-lg-0">''' + en_category_cards[
            category] + '''</div></div></div>'''
    print("en_search:", filtered_categories)
    return jsonify({'html': f'<div class="row gx-lg-5">{filtered_html}</div>'})


@app.route("/")
def homepage():
    clear_history()
    return render_template('index.html')


@app.route("/heb")
def heb_homepage():
    clear_history()
    return render_template('index_heb.html')




@app.route('/heb/<profession>', methods=['GET', 'POST'])
def start_heb_chat(profession):
    return start_chat(profession, lang="heb")


@app.route('/<profession>', methods=['GET', 'POST'])
def start_en_chat(profession):
    return start_chat(profession, lang="en")


@app.route('/<profession>/clear_conversation')
def clear_conversation(profession):
    global professions
    professions[profession]['messages'].clear()
    professions[profession]['messages'].append(professions[profession]['start prompt'])
    return redirect(url_for('start_en_chat', profession=profession))


@app.route('/heb/<profession>/clear_conversation')
def clear_heb_conversation(profession):
    global professions
    professions[profession]['messages'].clear()
    professions[profession]['messages'].append(professions[profession]['start prompt'])
    return redirect(url_for('start_heb_chat', profession=profession))



if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=3000)
