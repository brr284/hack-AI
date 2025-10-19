# hack-AI

<div align="center">

**Siber Güvenlik AI Asistanı | Cybersecurity AI Assistant**

⚠️ **IMPORTANT: Pollinations AI has content filters. For unrestricted usage, use local models (Ollama, LM Studio).** ⚠️

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)](https://github.com/brr284/hack-AI)

</div>

## 📋 Genel Bakış / Overview

**hack-AI**, siber güvenlik profesyonelleri ve araştırmacılar için geliştirilmiş, açık kaynaklı bir masaüstü AI asistanıdır. Pollinations AI API'sini kullanarak güvenlik testleri, kod analizi, exploit geliştirme ve penetrasyon testi araçları oluşturmanıza yardımcı olur.

**hack-AI** is an open-source desktop AI assistant designed for cybersecurity professionals and researchers. It leverages the Pollinations AI API to help you create security tests, analyze code, develop exploits, and build penetration testing tools.

## ✨ Özellikler / Features

### 🦠 Malware Analizi / Malware Analysis
Güvenlik araştırması için malware örnekleri ve davranış analizleri oluşturun.

### 🔓 Exploit Geliştirme / Exploit Development  
Güvenlik testleri için exploit kodları ve PoC (Proof of Concept) scriptleri geliştirin.

### 🔍 Penetrasyon Testi / Penetration Testing
Hedef sistemler için özelleştirilmiş pentest araçları ve otomatik scriptler oluşturun.

### 🛡️ Güvenlik Denetimi / Security Auditing
Kod güvenlik analizi yapın, zafiyetleri tespit edin ve düzeltme önerileri alın.

### 💬 Serbest Mod / Free Mode
Genel amaçlı AI destekli metin üretimi ve teknik danışmanlık.

## 🚀 Kurulum / Installation

### Gereksinimler / Requirements

- **Python**: 3.7 veya üzeri
- **İşletim Sistemi**: Windows, Linux (WSL)
- **Bağımlılıklar**: `requirements.txt` dosyasında listelendi

### Windows Kurulumu

```powershell
# Repository'yi klonlayın
git clone https://github.com/brr284/hack-AI.git
cd hack-AI

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Uygulamayı çalıştırın
hackai open
# veya
python hackai_app.py
```

### Linux / WSL Kurulumu

```bash
# Repository'yi klonlayın
git clone https://github.com/brr284/hack-AI.git
cd hack-AI

# Tkinter'ı yükleyin (gerekirse)
sudo apt update
sudo apt install -y python3-tk

# Python bağımlılıklarını yükleyin
pip install -r requirements.txt

# Launcher'ı çalıştırılabilir yapın
chmod +x hackai

# Uygulamayı başlatın
./hackai open
# veya
python3 hackai_app.py
```

## 💻 Kullanım / Usage

### Komut Satırı / Command Line

**Windows:**
```powershell
hackai open
```

**Linux:**
```bash
./hackai open
```

**Her İki Platform:**
```bash
python3 hackai_app.py
```

### Arayüz Kullanımı / Interface Guide

1. **Mod Seçimi**: Sol panelden bir operasyon modu seçin
   - 🦠 Malware: Malware analiz örnekleri
   - 🔓 Exploit: Exploit ve PoC kodları
   - 🔍 Pentest: Penetrasyon testi araçları
   - 🛡️ Audit: Kod güvenlik denetimi
   - 💬 Free: Serbest mod

2. **İstek Girişi**: Metin kutusuna detaylı açıklama girin

3. **Üretim**: "Oluştur" butonuna tıklayın ve AI'ın yanıtını bekleyin

4. **Kaydetme**: Sonucu "Kaydet" butonu ile dosyaya aktarın

## 🏗️ Mimari / Architecture

```
hack-AI/
├── hackai_app.py          # Ana GUI uygulaması (Tkinter)
├── pollinations_ai.py     # API istemci katmanı
├── hackai.bat             # Windows launcher
├── hackai                 # Linux launcher
├── requirements.txt       # Python bağımlılıkları
├── WARP.md               # Warp AI için geliştirici kılavuzu
└── README.md             # Proje dokümantasyonu
```

### Veri Akışı / Data Flow

1. Kullanıcı GUI'de mod seçer ve prompt girer
2. `hackai_app.py` isteği ilgili fonksiyona yönlendirir
3. `pollinations_ai.py` API çağrısını yapar
4. AI yanıtı GUI'ye stream edilir
5. Kullanıcı sonucu görüntüler ve kaydeder

## 🛠️ Teknolojiler / Technologies

- **Python 3.7+**: Ana programlama dili
- **Tkinter**: Cross-platform GUI framework
- **Pollinations AI API**: Text generation backend
- **Requests**: HTTP client library
- **Threading**: Asenkron işlemler için
- **Pillow**: Görüntü işleme (opsiyonel)

## 🤖 AI Model Limitations & Alternatives

### Current Issue

Pollinations AI has built-in content filters that may refuse certain security research requests. This is a limitation of the free API service.

### Solutions

#### Option 1: Use Alternative Prompts
The app includes jailbreak prompts in `pollinations_ai.py`, but results may vary.

#### Option 2: Local Uncensored Models (RECOMMENDED)

For **complete unrestricted control**, use local AI models:

**Quick Setup:**
```bash
# Install Ollama (5 minutes)
winget install Ollama.Ollama

# Download uncensored model
ollama pull dolphin-mixtral

# Start server
ollama serve
```

**Uncensored Models:**
- `dolphin-mixtral` - No restrictions
- `wizard-vicuna-uncensored` - Fully uncensored
- `nous-hermes` - Research-focused
- `alpaca-lora-uncensored` - Lightweight

**Integration:**
Modify `pollinations_ai.py` to point to `http://localhost:11434`

#### Option 3: Use `ai_backends.py`

The project includes `ai_backends.py` with:
- Multiple backend support
- Automatic refusal detection
- Fallback to working endpoints

```python
from ai_backends import AlternativeAI
ai = AlternativeAI()
result = ai.generate_unrestricted("your request")
```

#### Option 4: Direct API Access

**HuggingFace (Free):**
- Sign up: https://huggingface.co
- Get API token
- Use unrestricted models: `mistralai/Mixtral-8x7B-Instruct-v0.1`

**OpenRouter (Paid but Uncensored):**
- Multiple uncensored models
- Pay per use
- No content filtering

### Recommendation

**For serious security research, use local models.** They provide:
- ✅ Zero restrictions
- ✅ Complete privacy
- ✅ No API costs
- ✅ Full control over output
- ✅ Offline capability

---

## ⚠️ Yasal Uyarı / Legal Disclaimer

**🇹🇷 Türkçe:**

Bu yazılım **yalnızca eğitim, araştırma ve yasal güvenlik testleri** için tasarlanmıştır. Kullanıcılar, bu aracı yalnızca:

- Sahip oldukları sistemlerde
- Yazılı izin aldıkları hedeflerde  
- Yasal çerçeve içinde

kullanmalıdır. **Yetkisiz erişim, veri ihlali veya zararlı amaçlarla kullanımı kesinlikle yasaktır** ve kullanıcının sorumluluğundadır.

**🇬🇧 English:**

This software is designed **exclusively for education, research, and authorized security testing**. Users must only use this tool on:

- Systems they own
- Targets with written permission
- Within legal boundaries

**Unauthorized access, data breaches, or malicious use is strictly prohibited** and is the sole responsibility of the user.

## 📝 Lisans / License

MIT License - Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 🤝 Katkıda Bulunma / Contributing

Katkılarınızı bekliyoruz! Pull request göndermeden önce:

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## 📧 İletişim / Contact

- **GitHub**: [@brr284](https://github.com/brr284)
- **Issues**: [GitHub Issues](https://github.com/brr284/hack-AI/issues)

## 🙏 Teşekkürler / Acknowledgments

- [Pollinations AI](https://pollinations.ai/) - AI API sağlayıcı
- Tüm katkıda bulunanlara teşekkürler

---

<div align="center">

**⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!**

**Made with ❤️ for cybersecurity professionals**

</div>
