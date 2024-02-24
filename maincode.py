import tkinter as tk
from tkinter import simpledialog, messagebox
from math import sin, cos, radians

class PhysicsExerciseSolver:
    def __init__(self, root):
        self.root = root
        self.language = "English"
        self.root.title("Physics Exercise Solver")
        self.images = {
            "image1": tk.PhotoImage(file="1.png"),
            "image2": tk.PhotoImage(file="2.png"),
        }
        self.create_buttons()
        self.create_labels()

        self.resp11, self.resp12, self.resp13, self.resp14, self.resp15, self.resp16 = None, None, None, None, None, None
        self.screen1 = None

    def create_buttons(self):
        self.button1 = tk.Button(self.root, text=self.get_button_text("button1"), command=self.show_screen1)
        self.button1.grid(row=0, column=0)

        self.button2 = tk.Button(self.root, text=self.get_button_text("button2"), command=self.show_screen2)
        self.button2.grid(row=0, column=1)

        self.language_button = tk.Button(self.root, text=self.get_button_text("language_button"), command=self.toggle_language)
        self.language_button.grid(row=0, column=2)

    def create_labels(self):
        self.label1 = tk.Label(self.root, image=self.images["image1"])
        self.label1.grid(row=1, column=0)
        self.label2 = tk.Label(self.root, image=self.images["image2"])
        self.label2.grid(row=1, column=1)

    def toggle_language(self):
        self.language = "Greek" if self.language == "English" else "English"
        self.update_language()

    def update_language(self):
        self.button1.config(text=self.get_button_text("button1"))
        self.button2.config(text=self.get_button_text("button2"))
        self.language_button.config(text=self.get_button_text("language_button"))

    def get_button_text(self, button_name):
        button_text = {
            "button1": {
                "English": "Motion with Trapezoidal Shape",
                "Greek": "Κίνηση με τραπεζοειδή Σχήματα"
            },
            "button2": {
                "English": "Forces with Zero Resultant Force",
                "Greek": "Δυνάμεις με Μηδενική Αποτέλεσματα"
            },
            "language_button": {
                "English": "Αλλαγή γλώσσας/Change Language",
                "Greek": "Αλλαγή γλώσσας/Change Language"
            },
            "button11": {
                "English": "Set Δt",
                "Greek": "Ορισμός Δt"
            },
            "button12": {
                "English": "Set V",
                "Greek": "Ορισμός V"
            },
            "button_solution": {
                "English": "Solution",
                "Greek": "Λύση"
            },
            "screen2_buttonFset": {
                "English": "Set Force F, Angle φ, and Mass m",
                "Greek": "Ορισμός Δύναμης F, Γωνίας φ, και Μάζας m"
            },
            "screen12": {
                "English": "Forces Analysis",
                "Greek": "Ανάλυση Δυνάμεων"
            },
            "screen11": {
                "English": "Motion Analysis",
                "Greek": "Ανάλυση Κίνησης"
            }
        }
        return button_text[button_name][self.language]

    def show_screen1(self):
        self.screen1 = tk.Toplevel(self.root)
        self.screen1.title(self.get_button_text("button1"))

        button11 = tk.Button(self.screen1, text=self.get_button_text("button11"), command=self.ask_questions)
        button11.pack()

        button12 = tk.Button(self.screen1, text=self.get_button_text("button12"), command=self.ask_moar_questions)
        button12.pack()

        button_solution = tk.Button(self.screen1, text=self.get_button_text("button_solution"), command=self.show_screen11)
        button_solution.pack()

    def ask_questions(self):
        questions = {
            "English": ["Δt for the first phase:", "Δt for the second phase:", "Δt for the third phase:"],
            "Greek": ["Δt για την πρώτη φάση:", "Δt για τη δεύτερη φάση:", "Δt για την τρίτη φάση:"]
        }
        
        for i, question in enumerate(questions[self.language]):
            response = simpledialog.askfloat("Question", question)
            
            if response is None:
                return
            else:
                if i == 0:
                    self.resp11 = response
                elif i == 1:
                    self.resp12 = response
                elif i == 2:
                    self.resp13 = response

    def ask_moar_questions(self):
        questions = {
            "English": ["Enter initial V:", "Enter V at the end of the first phase:", "Enter V at the end of the second phase:", "Enter V at the end of the third phase:"],
            "Greek": ["Εισαγωγή αρχικού V:", "Εισαγωγή V στο τέλος της πρώτης φάσης:", "Εισαγωγή V στο τέλος της δεύτερης φάσης:", "Εισαγωγή V στο τέλος της τρίτης φάσης:"]
        }
        
        for i, question in enumerate(questions[self.language]):
            response = simpledialog.askfloat("Question", question)
            
            if response is None:
                return
            else:
                if i == 0:
                    self.resp14 = response
                elif i == 1:
                    self.resp15 = response
                elif i == 2:
                    self.resp16 = response
                elif i == 3:
                    self.resp17 = response

    def show_screen2(self):
        screen2 = tk.Toplevel(self.root)
        screen2.title(self.get_button_text("button2"))
        buttonFset = tk.Button(screen2, text=self.get_button_text("screen2_buttonFset"), command=self.ask_questionsS2)
        buttonFset.pack()
        buttonsolution = tk.Button(screen2, text=self.get_button_text("button_solution"), command=self.show_screen12)
        buttonsolution.pack()
   
    def ask_questionsS2(self):
        questions = {
            "English": ["Enter force F:", "Enter the components of angle φ:", "Enter the mass of the object m in kg:"],
            "Greek": ["Καταχώριση δύναμης F:", "Καταχώριση συνισταμένων γωνίας φ:", "Καταχώριση μάζας του αντικειμένου m σε kg:"]
        }
        
        for i, question in enumerate(questions[self.language]):
            response = simpledialog.askfloat("Question", question)
            
            if response is None:
                return
            else:
                if i == 0:
                    self.F = response
                elif i == 1:
                    self.w = response
                elif i == 2:
                    self.m = response

    def show_screen12(self):
        screen12 = tk.Toplevel(self.root)
        screen12.title(self.get_button_text("screen12"))

        w_in_radians = radians(self.w)

        imw = sin(w_in_radians)
        synw = cos(w_in_radians)
        imw = round(imw, 3)
        synw = round(synw, 3)

        Fy = imw * self.F
        Fx = synw * self.F
        self.W = self.m * 10
        self.N = self.W - Fy
        self.T = Fx

        if self.N < 0:
            errorS2 = 1
        else:
            errorS2 = 0
        if errorS2 == 0:
            label = tk.Label(screen12, text=f"Analyzing F into components: sinφ = Fy / F => Fy = sinφ * F => Fy = {Fy}" if self.language == "English" else f"Ανάλυση της F σε συνιστώσες: sinφ = Fy / F => Fy = sinφ * F => Fy = {Fy}") 
            label.pack()
            label2 = tk.Label(screen12, text=f"cosφ = Fx / F => Fx = cosφ * F => Fx = {Fx}" if self.language == "English" else f"cosφ = Fx / F => Fx = cosφ * F => Fx = {Fx}") 
            label2.pack()
            label3 = tk.Label(screen12, text=f"Finding the weight: W = m * g => W = {self.m} * 10 => W = {self.W}" if self.language == "English" else f"Υπολογισμός βάρους: W = m * g => W = {self.m} * 10 => W = {self.W}") 
            label3.pack()
            label4 = tk.Label(screen12, text=f"As the object has ΣF=0 it also has ΣN=0 => N = W - Fy => N = {self.W} - {Fy} => N = {self.N}" if self.language == "English" else f"Δεδομένου ότι το αντικείμενο έχει ΣF=0, έχει επίσης ΣN=0 => N = W - Fy => N = {self.W} - {Fy} => N = {self.N}") 
            label4.pack()
            label5 = tk.Label(screen12, text=f"As the object has ΣF=0 it also has ΣT=0 => T = Fx => T = {Fx}" if self.language == "English" else f"Δεδομένου ότι το αντικείμενο έχει ΣF=0, έχει επίσης ΣT=0 => T = Fx => T = {Fx}") 
            label5.pack()
        else:
            messagebox.showerror("Error", "The normal force is negative, please review your data.")

    def show_screen11(self):
        screen11 = tk.Toplevel(self.root)
        screen11.title(self.get_button_text("screen11"))
        t1 = self.resp11
        t2 = self.resp12
        t3 = self.resp13
        V1 = self.resp14
        V2 = self.resp15
        V3 = self.resp16
        x11f1 = self.resp15 - self.resp14
        x11f2 = self.resp16 - self.resp15
        x11f3 = self.resp17 - self.resp16
        a1 = x11f1 / self.resp11
        a2 = x11f2 / self.resp12
        a3 = x11f3 / self.resp13
        
        errorin1 = 0
        if x11f1 == 0:
            if self.resp14 < 0 and self.resp15 < 0:
                e1 = self.resp14 * self.resp11
            elif self.resp14 >= 0 and self.resp15 >= 0:
                e1 = self.resp14 * self.resp11
            else:
                errorin1 = 1
        else:
            if self.resp14 < 0 and self.resp15 > 0:
                errorin1 = 1
            elif self.resp14 > 0 and self.resp15 < 0:
                errorin1 = 1
            elif self.resp14 >= 0 and self.resp15 >= 0:
                e1 = self.resp14 * self.resp11 + ((self.resp15 - self.resp14) * self.resp11) / 2
            elif self.resp14 <= 0 and self.resp15 <= 0:
                e1 = self.resp14 * self.resp11 + ((self.resp15 - self.resp14) * self.resp11) / 2
            
            errorin2 = 0
        if x11f2 == 0:
            if self.resp15 < 0 and self.resp16 < 0:
                e2 = self.resp15 * self.resp12
            elif self.resp15 >= 0 and self.resp16 >= 0:
                e2 = self.resp15 * self.resp12
            else:
                errorin2 = 1
        else:
            if self.resp15 < 0 and self.resp16 > 0:
                errorin2 = 1
            elif self.resp15 > 0 and self.resp16 < 0:
                errorin2 = 1
            elif self.resp15 >= 0 and self.resp16 >= 0:
                e2 = self.resp15 * self.resp12 + ((self.resp16 - self.resp15) * self.resp12) / 2
            elif self.resp15 <= 0 and self.resp16 <= 0:
                e2 = self.resp15 * self.resp12 + ((self.resp16 - self.resp15) * self.resp12) / 2
        
        errorin3 = 0
        if x11f3 == 0:
            if self.resp16 < 0 and self.resp17 < 0:
                e3 = self.resp16 * self.resp13
            elif self.resp16 >= 0 and self.resp17 >= 0:
                e3 = self.resp16 * self.resp13
            else:
                errorin3 = 1
        else:
            if self.resp16 < 0 and self.resp17 > 0:
                errorin3 = 1
            elif self.resp16 > 0 and self.resp17 < 0:
                errorin3 = 1
            elif self.resp16 >= 0 and self.resp17 >= 0:
                e3 = self.resp16 * self.resp13 + ((self.resp17 - self.resp16) * self.resp13) / 2
            elif self.resp16 <= 0 and self.resp17 <= 0:
                e3 = self.resp16 * self.resp13 + ((self.resp17 - self.resp16) * self.resp13) / 2
        eol = e1 + e2 + e3
        
        x11f1 = self.resp15 - self.resp14
        x11f2 = self.resp16 - self.resp15
        x11f3 = self.resp17 - self.resp16
        if x11f1 > 0 and self.resp14 >= 0 and self.resp15 >= 0:
            label = tk.Label(screen11, text="This justification alone is sufficient to justify the type of motion in such exercises: In phase 1, the motion is uniformly accelerated because the slope of the graph is constant and the magnitude of the velocity increases." if self.language == "English" else f"Αυτή η αιτιολόγηση είναι από μόνη της αρκετή για να αιτιολογήσει κάποιος το είδος της κίνησης σε τέτοιες ασκήσεις: Στην φάση 1 η κίνηση είναι ομαλά επιταχυνόμενη, επειδή η κλίση της γραφικής παράστασης είναι σταθερή και το μέτρο της ταχύτητας αυξάνεται")
            label.pack()
        if x11f1 > 0 and self.resp14 < 0 and self.resp15 <= 0:
            label = tk.Label(screen11, text="This justification alone is sufficient to justify the type of motion in such exercises: In phase 1, the motion is uniformly decelerated because the slope of the graph is constant and the magnitude of the velocity decreases." if self.language == "English" else f"Αυτή η αιτιολόγηση είναι από μόνη της αρκετή για να αιτιολογήσει κάποιος το είδος της κίνησης σε τέτοιες ασκήσεις: Στην φάση 1 η κίνηση είναι ομαλά επιβραδυνόμενη, επειδή η κλίση της γραφικής παράστασης είναι σταθερή και το μέτρο της ταχύτητας μειώνεται")
            label.pack()
        if x11f1 < 0 and self.resp14 > 0 and self.resp15 >= 0:
            label = tk.Label(screen11, text="This justification alone is sufficient to justify the type of motion in such exercises: In phase 1, the motion is uniformly decelerated because the slope of the graph is constant and the magnitude of the velocity decreases." if self.language == "English" else f"Αυτή η αιτιολόγηση είναι από μόνη της αρκετή για να αιτιολογήσει κάποιος το είδος της κίνησης σε τέτοιες ασκήσεις: Στην φάση 1 η κίνηση είναι ομαλά επιβραδυνόμενη, επειδή η κλίση της γραφικής παράστασης είναι σταθερή και το μέτρο της ταχύτητας μειώνεται")
            label.pack()
        
        if x11f1 < 0 and self.resp14 <= 0 and self.resp15 <= 0:
            label = tk.Label(screen11, text="This justification alone is sufficient to justify the type of motion in such exercises: In phase 1, the motion is uniformly accelerated because the slope of the graph is constant and the magnitude of the velocity increases." if self.language == "English" else f"Αυτή η αιτιολόγηση είναι από μόνη της αρκετή για να αιτιολογήσει κάποιος το είδος της κίνησης σε τέτοιες ασκήσεις: Στην φάση 1 η κίνηση είναι ομαλά επιταχυνόμενη, επειδή η κλίση της γραφικής παράστασης είναι σταθερή και το μέτρο της ταχύτητας αυξάνεται")
            label.pack()
        if x11f1 == 0:
            label = tk.Label(screen11, text="In phase 1, the motion is uniformly straight because the velocity remains constant." if self.language == "English" else f" Στην φάση 1 η κίνηση είναι ευθήγραμμη ομαλή, επειδή η ταχύτητα παραμένει σταθερή")
            label.pack()
        
        if x11f2 > 0 and self.resp15 >= 0 and self.resp16 >= 0:
            label2 = tk.Label(screen11, text="In phase 2, the motion is uniformly accelerated because the slope of the graph is constant and the magnitude of the velocity increases." if self.language == "English" else f"        Στην φάση 2 η κίνηση είναι ομαλά επιταχυνόμενη, επειδή η κλίση της γραφικής παράστασης είναι σταθερή και το μέτρο της ταχύτητας αυξάνεται")
            label2.pack()
        if x11f2 > 0 and self.resp15 < 0 and self.resp16 <= 0:
            label2 = tk.Label(screen11, text="In phase 2, the motion is uniformly decelerated because the slope of the graph is constant and the magnitude of the velocity decreases." if self.language == "English" else f"        Στην φάση 2 η κίνηση είναι ομαλά επιβραδυνόμενη, επειδή η κλίση της γραφικής παράστασης είναι σταθερή και το μέτρο της ταχύτητας μειώνεται")
            label2.pack()
        if x11f2 < 0 and self.resp15 > 0 and self.resp16 >= 0:
            label2 = tk.Label(screen11, text="In phase 2, the motion is uniformly decelerated because the slope of the graph is constant and the magnitude of the velocity decreases." if self.language == "English" else f"        Στην φάση 2 η κίνηση είναι ομαλά επιβραδυνόμενη, επειδή η κλίση της γραφικής παράστασης είναι σταθερή και το μέτρο της ταχύτητας μειώνεται")
            label2.pack()
        if x11f2 < 0 and self.resp15 <= 0 and self.resp16 <= 0:
            label2 = tk.Label(screen11, text="In phase 2, the motion is uniformly accelerated because the slope of the graph is constant and the magnitude of the velocity increases." if self.language == "English" else f"        Στην φάση 2 η κίνηση είναι ομαλά επιταχυνόμενη, επειδή η κλίση της γραφικής παράστασης είναι σταθερή και το μέτρο της ταχύτητας αυξάνεται")
            label2.pack()
        if x11f2 == 0:
            label2 = tk.Label(screen11, text="In phase 2, the motion is uniformly straight because the velocity remains constant." if self.language == "English" else f"        Στην φάση 2 η κίνηση είναι ευθήγραμμη ομαλή, επειδή η ταχύτητα παραμένει σταθερή")
            label2.pack()
        if x11f3 > 0 and self.resp16 >= 0 and self.resp17 >= 0:
            label3 = tk.Label(screen11, text="n phase 3, the motion is uniformly accelerated because the slope of the graph is constant and the magnitude of the velocity increases." if self.language == "English" else f"        Στην φάση 3 η κίνηση είναι ομαλά επιταχυνόμενη, επειδή η κλίση της γραφικής παράστασης είναι σταθερή και το μέτρο της ταχύτητας αυξάνεται")
            label3.pack()
        if x11f3 > 0 and self.resp16 < 0 and self.resp17 <= 0:
            label3 = tk.Label(screen11, text="In phase 3, the motion is uniformly decelerated because the slope of the graph is constant and the magnitude of the velocity decreases." if self.language == "English" else f"        Στην φάση 3 η κίνηση είναι ομαλά επιβραδυνόμενη, επειδή η κλίση της γραφικής παράστασης είναι σταθερή και το μέτρο της ταχύτητας μειώνεται")
            label3.pack()
        if x11f3 < 0 and self.resp16 > 0 and self.resp17 >= 0:
            label3 = tk.Label(screen11, text="In phase 3, the motion is uniformly decelerated because the slope of the graph is constant and the magnitude of the velocity decreases." if self.language == "English" else f"        Στην φάση 3 η κίνηση είναι ομαλά επιβραδυνόμενη, επειδή η κλίση της γραφικής παράστασης είναι σταθερή και το μέτρο της ταχύτητας μειώνεται")
            label3.pack()
        if x11f3 < 0 and self.resp16 <= 0 and self.resp17 <= 0:
            label3 = tk.Label(screen11, text="In phase 3, the motion is uniformly accelerated because the slope of the graph is constant and the magnitude of the velocity increases." if self.language == "English" else f"        Στην φάση 3 η κίνηση είναι ομαλά επιταχυνόμενη, επειδή η κλίση της γραφικής παράστασης είναι σταθερή και το μέτρο της ταχύτητας αυξάνεται")
            label3.pack()
        if x11f3 == 0:
            label3 = tk.Label(screen11, text="In phase 3, the motion is uniformly straight because the velocity remains constant." if self.language == "English" else f"        Στην φάση 3 η κίνηση είναι ευθήγραμμη ομαλή, επειδή η ταχύτητα παραμένει σταθερή")
            label3.pack()

        label4 = tk.Label(screen11, text=f"Υπολογισμός της επιτάχυνσης: Φάση 1: a1 = Δv/Δt => a1 = Vτελικό - Vαρχικό / Δt => a1 = {self.resp15} - {self.resp14} / {self.resp11} => a1 = {a1}" if self.language == "Greek" else f"        Acceleration Calculation: Phase 1: a1 = Δv/Δt => a1 = Vfinal - Vinitial / Δt => a1 = {self.resp15} - {self.resp14} / {self.resp11} => a1 = {a1}")
        label4.pack()
        label5 = tk.Label(screen11, text=f"Φάση 2: a2 = Δv/Δt => a2 = Vτελικό - Vαρχικό / Δt => a2 = {self.resp16} - {self.resp15} / {self.resp12} => a2 = {a2}" if self.language == "Greek" else f"        Phase 2: a2 = Δv/Δt => a2 = Vfinal - Vinitial / Δt => a2 = {self.resp16} - {self.resp15} / {self.resp12} => a2 = {a2}")
        label5.pack()
        label6 = tk.Label(screen11, text=f"Φάση 3: a3 = Δv/Δt => a3 = Vτελικό - Vαρχικό / Δt => a3 = {self.resp17} - {self.resp16} / {self.resp13} => a3 = {a3}" if self.language == "Greek" else f"        Phase 3: a3 = Δv/Δt => a3 = Vfinal - Vinitial / Δt => a3 = {self.resp17} - {self.resp16} / {self.resp13} => a3 = {a3}")
        label6.pack()

        if errorin1 == 0:
            label6 = tk.Label(screen11, text=f"Displacement is found in the area at the end of the first phase and is {e1}" if self.language == "English" else f"Μετατόπιση της πρώτης φάσης βρίσκεται στο εμβαδόν και είναι {e1}") 
            label6.pack()
        else:
            label6 = tk.Label(screen11, text=f"Phase 1 has incorrect input" if self.language == "English" else f"Η Φάση 1 δεν έχει επιτρεπτές τιμές") 
            label6.pack()
        if errorin2 == 0:
            label7 = tk.Label(screen11, text=f"Displacement is found in the area at the end of the second phase and is {e2}" if self.language == "English" else f"Μετατόπιση της δεύτερης φάσης βρίσκεται στο εμβαδόν και είναι {e2}") 
            label7.pack()
        else:
            label7 = tk.Label(screen11, text=f"Phase 2 has incorrect input" if self.language == "English" else f"Η Φάση 2 δεν έχει επιτρεπτές τιμές") 
            label7.pack()
        if errorin3 == 0:
            label8 = tk.Label(screen11, text=f"Displacement is found in the area at the end of the third phase and is {e3}" if self.language == "English" else f"Μετατόπιση της τρίτης φάσης βρίσκεται στο εμβαδόν και είναι {e3}") 
            label8.pack()
        else:
            label8 = tk.Label(screen11, text=f"Phase 3 has incorrect input" if self.language == "English" else f"Η Φάση 3 δεν έχει επιτρεπτές τιμές") 
            label8.pack()
        if errorin1 == 0 and errorin2 == 0 and errorin3 == 0:
            label9 = tk.Label(screen11, text=f"Total Displacement of the motion is {eol}" if self.language == "English" else f"Ολική μετατόπιση όλης της κίνησης είναι {eol}") 
            label9.pack()
        else:
            label9 = tk.Label(screen11, text=f"At least one of the phases has incorrect input" if self.language == "English" else f"Τουλάχιστον μια φάση δεν έχει επιτρεπτές τιμές") 
            label9.pack()

root = tk.Tk()
app = PhysicsExerciseSolver(root)
root.mainloop()
