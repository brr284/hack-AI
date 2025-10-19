"""
Hack-AI - Siber Güvenlik Uzmanları İçin AI Aracı
Kullanım: hackai open
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from pollinations_ai import PollinationsAI, create_virus_sample, create_penetration_test_tool, analyze_vulnerability
import threading


class HackAIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hack-AI - Siber Güvenlik AI Asistanı")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a1a')
        
        self.ai = PollinationsAI()
        self.setup_ui()
        
    def setup_ui(self):
        # Başlık
        title_frame = tk.Frame(self.root, bg='#2d2d2d', height=60)
        title_frame.pack(fill=tk.X, padx=10, pady=10)
        
        title = tk.Label(
            title_frame, 
            text="🔒 Hack-AI - Siber Güvenlik AI Asistanı",
            font=('Arial', 18, 'bold'),
            bg='#2d2d2d',
            fg='#00ff00'
        )
        title.pack(pady=15)
        
        # Ana frame
        main_frame = tk.Frame(self.root, bg='#1a1a1a')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Sol panel - Kategori butonları
        left_panel = tk.Frame(main_frame, bg='#2d2d2d', width=200)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        tk.Label(
            left_panel,
            text="Araçlar",
            font=('Arial', 12, 'bold'),
            bg='#2d2d2d',
            fg='#ffffff'
        ).pack(pady=10)
        
        categories = [
            ("🦠 Malware Oluştur", self.malware_mode),
            ("🔓 Exploit Geliştir", self.exploit_mode),
            ("🔍 Güvenlik Testi", self.pentest_mode),
            ("🛡️ Kod Analizi", self.audit_mode),
            ("💬 Serbest Mod", self.free_mode),
        ]
        
        for text, command in categories:
            btn = tk.Button(
                left_panel,
                text=text,
                command=command,
                bg='#3d3d3d',
                fg='#00ff00',
                font=('Arial', 10),
                relief=tk.FLAT,
                cursor='hand2',
                width=20,
                pady=8
            )
            btn.pack(pady=5, padx=10)
        
        # Sağ panel - Ana çalışma alanı
        right_panel = tk.Frame(main_frame, bg='#1a1a1a')
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Üst bilgi
        self.info_label = tk.Label(
            right_panel,
            text="Mod Seçin",
            font=('Arial', 11),
            bg='#1a1a1a',
            fg='#888888'
        )
        self.info_label.pack(pady=5)
        
        # Giriş alanı
        input_frame = tk.Frame(right_panel, bg='#1a1a1a')
        input_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            input_frame,
            text="İstek:",
            font=('Arial', 10),
            bg='#1a1a1a',
            fg='#ffffff'
        ).pack(anchor=tk.W)
        
        self.input_text = scrolledtext.ScrolledText(
            input_frame,
            height=4,
            bg='#2d2d2d',
            fg='#ffffff',
            insertbackground='#00ff00',
            font=('Consolas', 10)
        )
        self.input_text.pack(fill=tk.X, pady=5)
        
        # Oluştur butonu
        self.generate_btn = tk.Button(
            right_panel,
            text="▶ Oluştur",
            command=self.generate,
            bg='#00ff00',
            fg='#000000',
            font=('Arial', 11, 'bold'),
            relief=tk.FLAT,
            cursor='hand2',
            pady=10
        )
        self.generate_btn.pack(pady=10)
        
        # Çıktı alanı
        output_frame = tk.Frame(right_panel, bg='#1a1a1a')
        output_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(
            output_frame,
            text="Çıktı:",
            font=('Arial', 10),
            bg='#1a1a1a',
            fg='#ffffff'
        ).pack(anchor=tk.W)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            bg='#2d2d2d',
            fg='#00ff00',
            insertbackground='#00ff00',
            font=('Consolas', 9)
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Kaydet butonu
        save_btn = tk.Button(
            right_panel,
            text="💾 Kaydet",
            command=self.save_output,
            bg='#3d3d3d',
            fg='#ffffff',
            font=('Arial', 9),
            relief=tk.FLAT,
            cursor='hand2'
        )
        save_btn.pack(pady=5)
        
        self.current_mode = "free"
        
    def malware_mode(self):
        self.current_mode = "malware"
        self.info_label.config(text="🦠 Malware Oluşturma Modu - Araştırma amaçlı")
        self.input_text.delete(1.0, tk.END)
        self.input_text.insert(1.0, "Örnek: Bir ransomware örneği oluştur...")
        
    def exploit_mode(self):
        self.current_mode = "exploit"
        self.info_label.config(text="🔓 Exploit Geliştirme Modu - Güvenlik testi için")
        self.input_text.delete(1.0, tk.END)
        self.input_text.insert(1.0, "Örnek: SQL injection exploit kodu yaz...")
        
    def pentest_mode(self):
        self.current_mode = "pentest"
        self.info_label.config(text="🔍 Penetrasyon Test Modu")
        self.input_text.delete(1.0, tk.END)
        self.input_text.insert(1.0, "Örnek: Web uygulaması tarama aracı oluştur...")
        
    def audit_mode(self):
        self.current_mode = "audit"
        self.info_label.config(text="🛡️ Kod Güvenlik Analizi Modu")
        self.input_text.delete(1.0, tk.END)
        self.input_text.insert(1.0, "Kod yapıştırın ve analiz edilsin...")
        
    def free_mode(self):
        self.current_mode = "free"
        self.info_label.config(text="💬 Serbest Mod - Her türlü istek")
        self.input_text.delete(1.0, tk.END)
        
    def generate(self):
        prompt = self.input_text.get(1.0, tk.END).strip()
        if not prompt:
            messagebox.showwarning("Uyarı", "Lütfen bir istek girin!")
            return
        
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Oluşturuluyor...\n\n")
        self.generate_btn.config(state=tk.DISABLED, text="⏳ Bekleyin...")
        
        def worker():
            try:
                if self.current_mode == "malware":
                    result = create_virus_sample(prompt)
                elif self.current_mode == "exploit":
                    result = self.ai.generate_exploit(prompt)
                elif self.current_mode == "pentest":
                    result = create_penetration_test_tool(prompt)
                elif self.current_mode == "audit":
                    result = self.ai.security_audit(prompt)
                else:
                    result = self.ai.generate_text(prompt)
                
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, result)
            except Exception as e:
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, f"Hata: {str(e)}")
            finally:
                self.generate_btn.config(state=tk.NORMAL, text="▶ Oluştur")
        
        thread = threading.Thread(target=worker)
        thread.daemon = True
        thread.start()
        
    def save_output(self):
        from tkinter import filedialog
        content = self.output_text.get(1.0, tk.END).strip()
        if not content:
            messagebox.showwarning("Uyarı", "Kaydedilecek içerik yok!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")]
        )
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            messagebox.showinfo("Başarılı", "Dosya kaydedildi!")


def main():
    root = tk.Tk()
    app = HackAIApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
