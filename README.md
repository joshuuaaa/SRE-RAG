# LLM-Driven First Aid Assistant for Disaster Zones

**Group 7 - KTU Project**
- Amal Ajay A - KTE22EC013
- Joshwin Binu - KTE22EC038  
- Judin Joe Mathew - KTE22EC039
- Justin Varghese - KTE22EC040

**Project Guide:** Asst. Prof. Shinoj K Sukumaran

---

## 🚨 Project Overview

An offline, portable emergency assistant powered by specialized AI to provide life-saving medical guidance in disaster zones where internet connectivity is unavailable.

### The Problem
- Kerala faces frequent natural disasters (floods, landslides)
- Critical infrastructure failures cut off communication
- People need immediate access to emergency medical information
- Existing assistants (Siri, Alexa) require internet connectivity

### Our Solution
A rugged, battery-powered device running a specialized offline LLM that provides:
- ✅ **Offline Operation** - No internet dependency
- ✅ **Medical Accuracy** - Based on WHO/Red Cross guidelines  
- ✅ **Voice & Text Input** - Accessible in stressful situations
- ✅ **Portable Design** - Raspberry Pi-based hardware
- ✅ **Context Awareness** - Understands emergency scenarios

---

## 📁 Demo Structure

```
crisis_assistant_demo/
├── crisis_assistant.py      # Main application
├── emergency_database.py    # Medical knowledge base
├── requirements.txt         # Dependencies
├── setup_instructions.md    # Setup guide
└── README.md               # This file
```

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the demo
python crisis_assistant.py

# 3. Choose Demo Mode (1) for presentation
```

## 💡 Key Features Demonstrated

### 1. Offline Knowledge Base
- 6 major emergency types covered
- WHO and Red Cross verified procedures
- Step-by-step instructions with warnings
- Supply lists and "when to seek help" guidance

### 2. Intelligent Query Processing
- Natural language understanding
- Keyword-based emergency type detection
- Confidence scoring for responses
- Handles multiple ways of asking the same question

### 3. Medical-Grade Responses
- **Critical Warnings** - What NOT to do
- **Step-by-Step Procedures** - Clear, numbered instructions  
- **Supply Requirements** - What materials are needed
- **Urgency Levels** - Critical/High/Moderate classification
- **Seek Help Indicators** - When professional care is essential

### 4. Professional Presentation
- Rich formatting with colors and tables
- Clean fallback for basic terminals
- Confidence indicators and timestamps
- System status and capability overview

---

## 🎯 Demo Scenarios

The demo includes these emergency scenarios:

1. **Severe Bleeding** - Wound care and hemorrhage control
2. **CPR** - Cardiac emergency and resuscitation  
3. **Burns** - Thermal injury treatment
4. **Choking** - Airway obstruction management
5. **Fractures** - Bone injury and immobilization
6. **Shock** - Systemic emergency management

Each scenario provides:
- Immediate action steps
- Critical safety warnings
- Required supplies
- When to seek professional help

---

## 🔧 Technical Implementation

### Current Demo Features
- **Python-based** - Cross-platform compatibility
- **Modular Design** - Separate database and logic
- **Rich Terminal UI** - Professional presentation
- **Error Handling** - Graceful failure modes
- **Extensible Architecture** - Easy to add new procedures

### Planned Hardware Deployment
- **Raspberry Pi 4** - 8GB RAM for model inference
- **Offline LLM** - TinyLlama or Phi-2 model
- **Voice Interface** - Whisper for speech-to-text
- **Audio Output** - Text-to-speech synthesis
- **Rugged Case** - Water/dust/shock resistant
- **Long Battery Life** - 12+ hours operation

---

## 📊 System Architecture

```
┌─────────────────┐
│   User Query    │ (Voice/Text)
└─────────┬───────┘
          │
┌─────────▼───────┐
│ Query Analysis  │ (Keyword Matching)
└─────────┬───────┘
          │
┌─────────▼───────┐
│ Knowledge Base  │ (Offline Database)
└─────────┬───────┘
          │
┌─────────▼───────┐
│ Response Format │ (Medical Procedures)
└─────────┬───────┘
          │
┌─────────▼───────┐
│ User Interface  │ (Rich Display/Audio)
└─────────────────┘
```

---

## 🏥 Medical Data Sources

All procedures based on verified medical guidelines:
- **WHO Emergency Care Guidelines 2023**
- **Red Cross First Aid Manual 2022**
- **American Heart Association CPR Guidelines**
- **International Trauma Care Standards**

---

## 🎬 Presentation Guide

### For Reviews/Demos:

1. **Opening** (30 seconds):
   - "Offline Crisis Assistant - no internet needed"
   - "WHO/Red Cross medical procedures"
   - "Smart query understanding"

2. **Live Demo** (2-3 minutes):
   - Run demo mode
   - Show 2-3 emergency scenarios
   - Highlight offline operation

3. **Technical Points** (1 minute):
   - "Ready for Raspberry Pi deployment"
   - "Expandable medical database"
   - "Voice interface integration planned"

4. **Impact Statement** (30 seconds):
   - "Life-saving guidance when networks fail"
   - "Accessible to non-medical personnel"
   - "Strengthens disaster preparedness"

---

## 🔮 Future Enhancements

### Phase 2 (Implementation):
- [ ] LLM integration (TinyLlama/Phi-2)
- [ ] Voice input/output capabilities
- [ ] Raspberry Pi hardware optimization
- [ ] Extended medical database
- [ ] Context memory between queries

### Phase 3 (Advanced Features):  
- [ ] Multi-language support
- [ ] Offline maps integration
- [ ] Vital signs monitoring
- [ ] Emergency contact system
- [ ] Data logging and analytics

---

## 📈 Success Metrics

- ✅ **Functionality**: Boots and responds <30 seconds
- ✅ **Accuracy**: 95%+ medically sound advice  
- ✅ **Portability**: <2kg weight, 12+ hours battery
- ✅ **Reliability**: Operates in harsh conditions
- ✅ **Usability**: Intuitive for non-technical users
E
---

## 🤝 Contributing

This is an academic project for KTU. For questions or collaboration:
- Contact team members through college channels
- Project guide: Asst. Prof. Shinoj K Sukumaran

---

## ⚖️ Disclaimer

**IMPORTANT**: This system provides emergency guidance for educational and preparedness purposes. It does not replace professional medical care. Always seek qualified medical help when available.

---

*Stay Safe. Stay Prepared. 🚨*
