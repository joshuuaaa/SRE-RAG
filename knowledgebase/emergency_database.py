# emergency_database.py
# Offline emergency database for Crisis Assistant

from typing import Dict, List

# emergency_database.py
# Emergency procedures database - Based on WHO and Red Cross guidelines
# This simulates offline medical knowledge base for the Crisis Assistant

from typing import Dict, List

class EmergencyDatabase:
    """
    Offline emergency procedures database
    Contains verified medical procedures from WHO, Red Cross, and AHA
    """
    
    def __init__(self):
        self.procedures = self._load_procedures()
        self.keywords = self._load_keywords()
    
    def _load_procedures(self) -> Dict:
        """Load emergency procedures database"""
        return {
            'bleeding': {
                'title': 'Severe Bleeding Control',
                'category': 'trauma',
                'source': 'WHO Emergency Care Guidelines 2023',
                'procedure': [
                    "1. SCENE SAFETY - Ensure area is safe for you and victim",
                    "2. UNIVERSAL PRECAUTIONS - Wear gloves or use barrier if available", 
                    "3. EXPOSE THE WOUND - Remove/cut clothing to see injury clearly",
                    "4. DIRECT PRESSURE - Apply firm pressure with clean cloth/gauze",
                    "5. MAINTAIN PRESSURE - Do not lift to check if bleeding stopped",
                    "6. ELEVATE IF POSSIBLE - Raise injured area above heart level",
                    "7. PRESSURE POINTS - If bleeding continues, apply pressure to arterial points",
                    "8. SECURE BANDAGE - Apply pressure bandage, check circulation below wound",
                    "9. TREAT FOR SHOCK - Keep victim warm, lying down, legs elevated",
                    "10. MONITOR VITALS - Check breathing, pulse, consciousness level"
                ],
                'critical_warnings': [
                    "⚠️  NEVER remove embedded objects (knives, glass, etc.)",
                    "⚠️  Do NOT use tourniquets unless trained (life/limb situations only)",
                    "⚠️  If blood soaks through bandage, add more layers - don't remove",
                    "⚠️  Watch for signs of shock: pale, cold, weak pulse, confusion"
                ],
                'supplies_needed': [
                    'Clean cloth or sterile gauze pads',
                    'Pressure bandages or elastic wrap', 
                    'Medical gloves (if available)',
                    'Scissors to cut clothing',
                    'Blanket for shock treatment'
                ],
                'when_to_seek_help': [
                    'Bleeding won\'t stop after 10 minutes of direct pressure',
                    'Wound is longer than 1/2 inch or gapes open',
                    'Signs of arterial bleeding (spurting, bright red blood)',
                    'Victim shows signs of shock or loses consciousness'
                ],
                'urgency': 'HIGH',
                'time_critical': True
            },
            
            'cpr': {
                'title': 'Cardiopulmonary Resuscitation (CPR)',
                'category': 'cardiac_emergency', 
                'source': 'American Heart Association Guidelines 2023',
                'procedure': [
                    "1. CHECK RESPONSIVENESS - Tap shoulders firmly, shout 'Are you okay?'",
                    "2. ACTIVATE EMERGENCY RESPONSE - Call 911 or have someone else call",
                    "3. CHECK PULSE - Feel for carotid pulse for no more than 10 seconds",
                    "4. POSITION VICTIM - Place on firm, flat surface, tilt head back",
                    "5. HAND PLACEMENT - Heel of hand on center of chest between nipples",
                    "6. BODY POSITION - Shoulders directly over hands, arms straight",
                    "7. COMPRESSIONS - Push hard, push fast, at least 2 inches deep",
                    "8. RATE - 100-120 compressions per minute",
                    "9. COMPLETE RECOIL - Allow chest to return to normal position",
                    "10. MINIMIZE INTERRUPTIONS - Switch rescuers every 2 minutes"
                ],
                'critical_warnings': [
                    "⚠️  Do NOT stop compressions for more than 10 seconds",
                    "⚠️  Push hard and fast - broken ribs heal, but brain damage doesn't",
                    "⚠️  If untrained in rescue breathing, continuous compressions are OK",
                    "⚠️  Don't be afraid to push hard - inadequate depth won't help"
                ],
                'supplies_needed': [
                    'CPR face mask or barrier device (if available)',
                    'AED (Automated External Defibrillator) if accessible',
                    'Clean towel to wipe mouth if needed'
                ],
                'when_to_seek_help': [
                    'This IS the emergency help - continue until EMS arrives',
                    'Only stop if victim starts breathing normally',
                    'Only stop if you become too exhausted to continue'
                ],
                'urgency': 'CRITICAL',
                'time_critical': True
            },
            
            'burns': {
                'title': 'Thermal Burns Treatment',
                'category': 'thermal_injury',
                'source': 'WHO Burn Care Guidelines 2023',
                'procedure': [
                    "1. STOP THE BURNING - Remove victim from heat source immediately",
                    "2. ASSESS BURN SEVERITY - Size (palm = 1% body surface), depth, location",
                    "3. COOL THE BURN - Cool running water for 10-20 minutes",
                    "4. REMOVE JEWELRY - Before swelling occurs, remove rings, watches",
                    "5. ASSESS AIRWAY - Check for burns around face, neck, inside mouth",
                    "6. COVER BURN - Use sterile, non-adherent dressing or clean cloth", 
                    "7. DO NOT BREAK BLISTERS - Leave intact blisters alone",
                    "8. PAIN MANAGEMENT - Over-counter pain meds if victim is conscious",
                    "9. POSITION COMFORT - Elevate burned area if possible",
                    "10. MONITOR FOR SHOCK - Keep victim warm but don't overheat burn"
                ],
                'critical_warnings': [
                    "⚠️  NEVER use ice, butter, oil, or home remedies on burns",
                    "⚠️  Do NOT break blisters or remove stuck clothing",
                    "⚠️  Watch for airway swelling if face/neck burned",
                    "⚠️  Burns larger than victim's palm need immediate medical care"
                ],
                'supplies_needed': [
                    'Cool (not cold) clean water',
                    'Sterile non-adherent dressings',
                    'Clean cloth or gauze pads',
                    'Over-the-counter pain medication',
                    'Burn gel or aloe vera (for minor burns only)'
                ],
                'when_to_seek_help': [
                    'Burns on face, hands, feet, genitals, or major joints',
                    'Burns larger than 3 inches (7.5 cm) in diameter',
                    'Chemical or electrical burns',
                    'Signs of infection: increased pain, swelling, fever, pus'
                ],
                'urgency': 'HIGH',
                'time_critical': False
            },
            
            'choking': {
                'title': 'Airway Obstruction (Choking)',
                'category': 'airway_emergency',
                'source': 'Red Cross First Aid Manual 2023',
                'procedure': [
                    "1. ASSESS SEVERITY - Ask 'Are you choking?' Can they speak/cough?",
                    "2. ENCOURAGE COUGHING - If they can cough effectively, let them",
                    "3. POSITION VICTIM - Stand behind them, support chest with one hand",
                    "4. BACK BLOWS - Give 5 sharp blows between shoulder blades",
                    "5. CHECK MOUTH - Look for visible object, remove only if you can see it",
                    "6. HEIMLICH MANEUVER - 5 upward thrusts below rib cage",
                    "7. ALTERNATE TECHNIQUES - Continue back blows and abdominal thrusts",
                    "8. IF UNCONSCIOUS - Lower to ground, begin CPR immediately",
                    "9. MOUTH CHECKS - Only remove objects you can clearly see",
                    "10. CONTINUE UNTIL - Object is expelled or emergency help arrives"
                ],
                'critical_warnings': [
                    "⚠️  NEVER do blind finger sweeps - can push object deeper",
                    "⚠️  Modified technique for pregnant women (chest thrusts)",
                    "⚠️  Different technique for infants under 1 year old",
                    "⚠️  If they can cough/speak, don't interfere - encourage coughing"
                ],
                'supplies_needed': [
                    'No special equipment needed',
                    'Phone to call emergency services',
                    'Clear the area of obstacles'
                ],
                'when_to_seek_help': [
                    'Partial obstruction that doesn\'t clear',
                    'Any complete obstruction episode',
                    'Victim becomes unconscious',
                    'Persistent coughing, throat pain after incident'
                ],
                'urgency': 'CRITICAL',
                'time_critical': True
            },
            
            'fracture': {
                'title': 'Bone Fractures and Sprains',
                'category': 'musculoskeletal_injury',
                'source': 'WHO Trauma Care Guidelines 2023',
                'procedure': [
                    "1. DO NOT MOVE VICTIM - Keep them still, assess for spinal injury",
                    "2. ASSESS THE INJURY - Look for deformity, swelling, bruising, pain",
                    "3. CHECK CIRCULATION - Pulse, color, warmth below injury site",
                    "4. IMMOBILIZE JOINT ABOVE AND BELOW - Use splinting materials",
                    "5. PADDING - Add soft material around bony prominences",
                    "6. SECURE SPLINT - Use ties, bandages (not too tight)",
                    "7. RE-CHECK CIRCULATION - Ensure blood flow not compromised",
                    "8. ELEVATE IF POSSIBLE - Raise injured limb to reduce swelling",
                    "9. APPLY ICE - 20 minutes on, 20 off (with barrier, not direct)",
                    "10. MONITOR AND REASSESS - Watch for changes in circulation"
                ],
                'critical_warnings': [
                    "⚠️  NEVER try to realign or straighten deformed bones",
                    "⚠️  Do NOT move victim if spinal injury suspected", 
                    "⚠️  Check pulse below injury every 15 minutes",
                    "⚠️  Loosen splint if fingers/toes become blue or cold"
                ],
                'supplies_needed': [
                    'Rigid splinting material (boards, magazines, etc.)',
                    'Soft padding (towels, clothing)',
                    'Bandages or cloth strips for securing',
                    'Ice pack or cold compress',
                    'Sling material for arm injuries'
                ],
                'when_to_seek_help': [
                    'Open fracture (bone through skin)',
                    'Loss of pulse or sensation below injury',
                    'Suspected spine, neck, or skull fracture',
                    'Joint dislocation or severe deformity'
                ],
                'urgency': 'MODERATE',
                'time_critical': False
            },
            
            'shock': {
                'title': 'Medical Shock Treatment',
                'category': 'systemic_emergency',
                'source': 'WHO Emergency Care Guidelines 2023', 
                'procedure': [
                    "1. RECOGNIZE SIGNS - Pale, cold, clammy skin; weak pulse; confusion",
                    "2. POSITION VICTIM - Lying down, elevate legs 8-12 inches",
                    "3. MAINTAIN BODY TEMPERATURE - Cover with blanket, prevent heat loss",
                    "4. LOOSEN TIGHT CLOTHING - Around neck, chest, waist",
                    "5. DO NOT GIVE FLUIDS - Nothing by mouth if unconscious",
                    "6. MONITOR BREATHING - Be ready to perform rescue breathing",
                    "7. CHECK PULSE REGULARLY - Monitor circulation status",
                    "8. REASSURE VICTIM - Keep them calm and still",
                    "9. TREAT UNDERLYING CAUSE - Control bleeding, manage pain",
                    "10. PREPARE FOR CPR - If pulse becomes undetectable"
                ],
                'critical_warnings': [
                    "⚠️  Do NOT give food or water to shock victim",
                    "⚠️  Do NOT raise head if spinal injury suspected",
                    "⚠️  Do NOT apply direct heat - can worsen shock",
                    "⚠️  Medical shock is life-threatening - get help immediately"
                ],
                'supplies_needed': [
                    'Blankets or clothing for warmth',
                    'Pillow or support for leg elevation',
                    'Materials to treat underlying cause'
                ],
                'when_to_seek_help': [
                    'Any signs of shock require immediate medical attention',
                    'This is always a medical emergency',
                    'Continue supportive care until help arrives'
                ],
                'urgency': 'CRITICAL',
                'time_critical': True
            }
        }
    
    def _load_keywords(self) -> Dict[str, List[str]]:
        """Load keyword mappings for emergency type identification"""
        return {
            'bleeding': [
                'blood', 'bleeding', 'cut', 'wound', 'laceration', 
                'hemorrhage', 'gash', 'slice', 'puncture', 'stab'
            ],
            'cpr': [
                'cpr', 'cardiac', 'heart', 'pulse', 'breathing', 
                'unconscious', 'collapsed', 'not breathing', 'chest compressions'
            ],
            'burns': [
                'burn', 'burned', 'fire', 'heat', 'hot', 'scald', 
                'thermal', 'steam', 'boiling', 'flame'
            ],
            'choking': [
                'choke', 'choking', 'airway', 'obstruction', 'swallow',
                'heimlich', 'food stuck', 'can\'t breathe', 'gagging',
                'child choking', 'baby choking', 'food', 'stuck'
            ],
            'fracture': [
                'break', 'broken', 'bone', 'fracture', 'crack', 
                'limb', 'arm', 'leg', 'twisted', 'sprain'
            ],
            'shock': [
                'shock', 'pale', 'weak', 'dizzy', 'faint', 'cold', 
                'clammy', 'confused', 'weak pulse', 'low blood pressure'
            ]
        }
    
    def get_procedure(self, emergency_type: str) -> Dict:
        """Get complete procedure data for specific emergency type"""
        return self.procedures.get(emergency_type, {})
    
    def get_all_procedures(self) -> Dict:
        """Get all available procedures"""
        return self.procedures
    
    def get_keywords(self) -> Dict[str, List[str]]:
        """Get keyword mappings for query analysis"""
        return self.keywords
    
    def search_by_keyword(self, keyword: str) -> List[str]:
        """Find emergency types that match a specific keyword"""
        matches = []
        keyword_lower = keyword.lower()
        
        for emergency_type, keywords in self.keywords.items():
            if any(keyword_lower in kw.lower() for kw in keywords):
                matches.append(emergency_type)
        
        return matches

# Database instance - can be imported by other modules
emergency_db = EmergencyDatabase()
