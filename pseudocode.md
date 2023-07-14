# Evercraft Pseudocode

## Description
You will work directly with a partner this week to complete as many iterations of the Evercraft project, using the python language, as you can. Your partner and you will trade on and off on the writing of tests for Test Driven Development (TDD) and the code that will be executed.

## Moscow

### Must have:
Name for a character
Character alignment
Character armor class and hit points
Character is able to attack
Character can be hit (damaged)
Character has ability scores (modifiers)
Character ability modifiers can modify attributes
Character can gain experience
Character can level up
Character can have classes

### Should have:
Character can choose a race
Character can have different weapons, armor, and items

### Could have:
Working dice rolls

### Won't have:
Lasers shooting out of someone's eyes
AI

## Iteration One

### Agile Stories

* As an anonymous user, I want to put a name for my character, so that I am distinguished from others
* As an anonymous user, I want to have an alignment for my character, so that I can choose how my character acts in game
* As an anonymous user, I want armor classes and hit points, so that I know how much damage I can take before I die
* As an anonymous user, I want my character to be able to be hit, so that there is risk involved when doing actions
* As an anonymous user, I want ability scores, so that each action per character is different than others
* As an anonymous user, I want my character to be able to gain experience, so that when I finish a battle I am able to improve from it
* As an anonymous user, I want my character to be able to level up, so that I can gain new skills throughout my time playing the game

### Procedural
START

Import modules if needed, 
Initialize Variables, 
Define Functions, 
Define Test Functions, 

END

### Functional
__init__:

Initialize the default values for the character's attributes.

get_name: <br>
Returns the name of the character.

set_name: <br>
Sets the name of the character.

get_alignment: <br>
Returns the alignment of the character.

set_alignment: <br>
Sets the alignment of the character.

get_armor_class: <br>
Returns the armor class of the character.

set_armor_class: <br>
Sets the armor class of the character.

get_hit_points: <br>
Returns the current hit points of the character.

set_hit_points: <br>
Sets the hit points of the character.

attack: <br>
Checks if the character's attack against an enemy is successful.

damage_taken: <br>
Calculates the damage taken by the character

is_alive: <br>
Checks if the character is alive.

get_strength: <br>
Returns the strength ability of the character.

get_dexterity: <br>
Returns the dexterity ability of the character.

get_constitution: <br>
Returns the constitution ability of the character.

get_wisdom: <br>
Returns the wisdom ability of the character.

get_intelligence: <br>
Returns the intelligence ability of the character.

get_charisma: <br>
Returns the charisma ability of the character.

set_ability_score: <br>
Sets the value of an ability.

change_ability_score: <br>
Changes the value of an ability with a modifier.

get_strength_modifier: <br>
Returns the strength modifier of the character.

get_dexterity_modifier: <br>
Returns the dexterity modifier of the character.
get_constitution_modifier: <br>
Returns the constitution modifier of the character.

gain_experience: <br>
Increases the character's experience points.

get_experience_points: <br>
Returns the current experience points of the character.

get_level: <br>
Returns the current level of the character.

set_level: <br>
Sets the level of the character.

get_experience_needed_for_level_up: <br>
Returns the amount of experience points needed to reach the next level.

level_up: <br>
Increases the character's level and modifies the hit points.

## Iteration Two

### Agile Stories
* As an anonymous user, I want my character to have classes, so that when other play with me, or I start a new game it will be different
* As an anonymous user I want to play a Fighter so that I can kick ass and take names
* As an anonymous user I want to play a Rogue so that I can defeat my enemies with finesse
* As an anonymous user I want to play a Monk so that I can enjoy being an Asian martial-arts archetype in a Medieval European setting
* As an anonymous user I want to play a Paladin so that I can smite evil, write wrongs, and be a self-righteous jerk

### Procedural
START

Import modules if needed
Initialize Variables
Define Functions
Define Test Functions

END

### Functional

#### Classes:
* Character: Represents a character in the game. Attributes: name, class, level, hit points, alignment. Methods: attack(), take_damage(), calculate_armor_class(), level_up().

* Fighter: Subclass of Character, representing the Fighter class. Overrides or extends methods from the Character class to customize capabilities specific to the Fighter class.

* Rogue: Subclass of Character, representing the Rogue class. Overrides or extends methods from the Character class to customize capabilities specific to the Rogue class.

* Monk: Subclass of Character, representing the Monk class. Overrides or extends methods from the Character class to customize capabilities specific to the Monk class.

* Paladin: Subclass of Character, representing the Paladin class. Overrides or extends methods from the Character class to customize capabilities specific to the Paladin class.

#### Functions:

calculate_attack_bonus: <br>
Calculates the attack bonus for a character based on their level and class.

calculate_damage: <br>
Calculates the damage dealt by a character based on their level and class.
  
calculate_critical_damage: <br>
Calculates the critical damage for a character based on their class and base damage.
  
calculate_armor_class: <br>
Calculates the armor class for a character based on their class and attributes.