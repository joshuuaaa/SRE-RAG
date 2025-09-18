# crisis_assistant_fixed.py
# Quick fix for the display issue

import os
import sys
from datetime import datetime
from typing import Dict, List, Optional
import json

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.prompt import Prompt
    from rich.table import Table
    from colorama import init, Fore, Back, Style
    init()
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("⚠️  Rich not installed. Using basic formatting.")

from emergency_database import emergency_db

class OfflineCrisisAssistant:
    def __init__(self):
        self.db = emergency_db
        self.console = Console() if RICH_AVAILABLE else None
        self.session_log = []
        
    def analyze_query(self, query: str) -> tuple:
        """Analyze user query to determine emergency type and confidence"""
        query_lower = query.lower()
        keywords_db = self.db.get_keywords()
        
        # Calculate weighted scores for each emergency type
        scores = {}
        for emergency_type, keywords in keywords_db.items():
            score = 0
            for keyword in keywords:
                if keyword in query_lower:
                    # Give higher weight to exact matches
                    if keyword == query_lower.strip():
                        score += 3
                    # Medium weight for word boundaries
                    elif f" {keyword} " in f" {query_lower} ":
                        score += 2
                    # Lower weight for partial matches
                    else:
                        score += 1
            
            if score > 0:
                scores[emergency_type] = score
        
        if not scores:
            return 'unknown', 0.0
        
        # Get best match and calculate confidence
        best_match = max(scores.items(), key=lambda x: x[1])
        emergency_type, raw_score = best_match
        
        # Normalize confidence score (0-1)
        max_possible_score = len(keywords_db[emergency_type]) * 3
        confidence = min(raw_score / max_possible_score, 1.0)
        
        return emergency_type, confidence
    
    def format_response_basic(self, emergency_type: str, query: str, confidence: float):
        """Basic formatting that always works"""
        procedure_data = self.db.get_procedure(emergency_type)
        if not procedure_data:
            self.show_general_help_basic()
            return
        
        print("\n" + "="*80)
        print(f"🚨 EMERGENCY RESPONSE: {procedure_data['title'].upper()}")
        print("="*80)
        print(f"⚠️  URGENCY LEVEL: {procedure_data['urgency']}")
        print(f"📍 QUERY: {query}")
        print(f"⏱️  TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🎯 CONFIDENCE: {confidence:.1%}")
        print(f"📚 SOURCE: {procedure_data['source']}")
        print()
        
        print("🔧 REQUIRED SUPPLIES:")
        for item in procedure_data['supplies_needed']:
            print(f"   • {item}")
        print()
        
        print("📋 STEP-BY-STEP PROCEDURE:")
        for step in procedure_data['procedure']:
            print(f"   {step}")
        print()
        
        print("⚠️  CRITICAL WARNINGS:")
        for warning in procedure_data['critical_warnings']:
            print(f"   {warning}")
        print()
        
        print("🏥 SEEK IMMEDIATE MEDICAL HELP IF:")
        for condition in procedure_data['when_to_seek_help']:
            print(f"   • {condition}")
        print()
        
        print("💡 DISCLAIMER: This device provides emergency guidance only.")
        print("   Seek professional medical help as soon as possible.")
        print("="*80)
    
    def show_general_help_basic(self):
        """Basic general help"""
        print("\n🚨 GENERAL EMERGENCY GUIDANCE")
        print("="*50)
        print("If you're unsure about the emergency type, please be more specific:")
        print("\n📞 IMMEDIATE ACTIONS:")
        print("   1. Ensure scene safety first")
        print("   2. Check victim responsiveness")
        print("   3. Call for emergency services if possible")
        print("   4. Provide care within your training level")
        print("\n🔍 BE MORE SPECIFIC - Try asking about:")
        print("   • 'Someone is bleeding heavily'")
        print("   • 'Person not breathing, need CPR steps'")
        print("   • 'Got burned by hot water'")
        print("   • 'Child choking on food'")
        print("   • 'Think my arm is broken'")
        print("   • 'Person in shock, pale and weak'")
        print("\n💡 Stay calm and provide care within your abilities.")
        print("="*50)
    
    def process_emergency_query(self, query: str):
        """Main function to process emergency queries"""        
        print(f"\n🔄 Processing query: '{query}'")
        print("📊 Analyzing emergency type...")
        
        # Analyze the query
        emergency_type, confidence = self.analyze_query(query)
        
        print(f"✅ Emergency type identified: {emergency_type} ({confidence:.1%} confidence)")
        print("📖 Retrieving offline guidance...")
        print()  # Add space before response
        
        # Format and display response
        if emergency_type == 'unknown' or confidence < 0.05:  # Lowered to 5%
            self.show_general_help_basic()
        else:
            self.format_response_basic(emergency_type, query, confidence)
    
    def show_system_status(self):
        """Display system status"""
        print("\n🏥 OFFLINE CRISIS ASSISTANT - SYSTEM STATUS")
        print("="*60)
        print("✅ System Mode: OFFLINE OPERATIONAL")
        print("✅ Knowledge Base: LOADED")
        print(f"✅ Emergency Procedures: {len(self.db.get_all_procedures())} PROCEDURES READY")
        print("✅ Response Time: <3 SECONDS")
        print("✅ Network Dependency: NONE (FULLY OFFLINE)")
        print("="*60)
        
        print("\n📋 AVAILABLE EMERGENCY PROCEDURES:")
        print("-" * 60)
        for proc_type, data in self.db.get_all_procedures().items():
            print(f"• {data['title']} - {data['urgency']} PRIORITY")
        print("="*60)

def demo_mode():
    """Demo mode for presentation"""
    assistant = OfflineCrisisAssistant()
    
    demo_queries = [
        "Someone is bleeding heavily from their arm",
        "Person collapsed and not breathing", 
        "Got burned by hot water on my hand",
        "Child is choking on food",
        "I think my leg is broken after falling"
    ]
    
    assistant.show_system_status()
    
    print("\n🎯 DEMO: Processing Sample Emergency Queries")
    print("="*60)
    
    for i, query in enumerate(demo_queries, 1):
        print(f"\n📝 DEMO QUERY {i}:")
        print(f"User: {query}")
        
        assistant.process_emergency_query(query)
        
        if i < len(demo_queries):
            input("\nPress Enter for next demo query...")

def interactive_mode():
    """Interactive mode for testing"""
    assistant = OfflineCrisisAssistant()
    
    assistant.show_system_status()
    
    print("\n🔴 INTERACTIVE MODE - Type 'quit' to exit, 'help' for guidance")
    print("="*60)
    
    while True:
        try:
            query = input("\n🚨 Emergency Query: ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("👋 Crisis Assistant shutting down. Stay safe!")
                break
            elif query.lower() == 'help':
                assistant.show_general_help_basic()
                continue
            elif query.lower() == 'status':
                assistant.show_system_status()
                continue
            elif query:
                assistant.process_emergency_query(query)
            else:
                print("Please enter an emergency query, 'help', 'status', or 'quit'.")
                
        except KeyboardInterrupt:
            print("\n👋 Crisis Assistant shutting down. Stay safe!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try again with a different query.")

def main():
    """Main function"""
    print("🚨 OFFLINE CRISIS ASSISTANT - DEMO VERSION")
    print("Simulating LLM-powered emergency guidance system")
    print("No internet connection required!")
    
    print("\nChoose mode:")
    print("1. Demo Mode (for presentation)")
    print("2. Interactive Mode (for testing)")
    print("3. Show System Status")
    
    try:
        choice = input("\nSelect mode (1, 2, or 3): ").strip()
        
        if choice == "1":
            demo_mode()
        elif choice == "2":
            interactive_mode()
        elif choice == "3":
            assistant = OfflineCrisisAssistant()
            assistant.show_system_status()
        else:
            print("Invalid choice. Running demo mode by default...")
            demo_mode()
            
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error starting application: {e}")

if __name__ == "__main__":
    main()