import secrets
import argparse
import sys
from pathlib import Path

if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'replace')


class PhrasePassGenerator:
    def __init__(self, languages='fr'):
        if isinstance(languages, str):
            languages = [languages]
        self.languages = languages
        self.words = self._load_dictionaries(languages)
        
    def _load_dictionaries(self, languages):
        all_words = []
        for language in languages:
            dict_path = Path(__file__).parent / 'dictionaries' / f'{language}.txt'
            if not dict_path.exists():
                raise FileNotFoundError(f"Dictionary file not found: {dict_path}")
            
            with open(dict_path, 'r', encoding='utf-8') as f:
                words = [line.strip() for line in f if line.strip()]
                all_words.extend(words)
        
        if len(all_words) < 10:
            print(f"Warning: Dictionary contains only {len(all_words)} words. Recommended: 1000+")
        
        return all_words
    
    def generate(self, word_count=4, separator='-', capitalize=False):
        if word_count < 1:
            raise ValueError("Word count must be at least 1")
        
        selected_words = [secrets.choice(self.words) for _ in range(word_count)]
        if capitalize:
            selected_words = [word.capitalize() for word in selected_words]
        return separator.join(selected_words)
    
    def get_entropy(self, word_count):
        import math
        if len(self.words) == 0:
            return 0
        return word_count * math.log2(len(self.words))


def main():
    parser = argparse.ArgumentParser(
        description='Generate secure passphrases from word dictionaries'
    )
    parser.add_argument(
        '-l', '--language',
        default='fr',
        help='Dictionary language(s): fr, en, or "fr,en" to mix both (default: fr)'
    )
    parser.add_argument(
        '-w', '--words',
        type=int,
        default=4,
        help='Number of words in passphrase (default: 4)'
    )
    parser.add_argument(
        '-s', '--separator',
        default='-',
        nargs='?',
        const='',
        help='Separator between words (default: -). Use -s without value for no separator'
    )
    parser.add_argument(
        '-c', '--count',
        type=int,
        default=1,
        help='Number of passphrases to generate (default: 1)'
    )
    parser.add_argument(
        '--entropy',
        action='store_true',
        help='Show entropy information'
    )
    parser.add_argument(
        '-C', '--capitalize',
        action='store_true',
        help='Capitalize the first letter of each word'
    )
    
    args = parser.parse_args()
    
    try:
        languages = [lang.strip() for lang in args.language.replace(' ', ',').split(',')]
        for lang in languages:
            if lang not in ['fr', 'en']:
                print(f"Error: Unknown language '{lang}'. Choose from: fr, en")
                return 1
        
        generator = PhrasePassGenerator(languages=languages)
        
        if args.entropy:
            entropy = generator.get_entropy(args.words)
            print(f"Languages: {', '.join(generator.languages)}")
            print(f"Dictionary size: {len(generator.words)} words")
            print(f"Entropy: {entropy:.2f} bits ({args.words} words)")
            print()
        
        for _ in range(args.count):
            passphrase = generator.generate(
                word_count=args.words,
                separator=args.separator,
                capitalize=args.capitalize
            )
            print(passphrase)
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
