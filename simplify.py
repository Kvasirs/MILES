import sys
import getopt

from simplifier import models
from simplifier import config
from simplifier import simplifier

if __name__ == '__main__':

    # If command line arguments are included.
    if len(sys.argv) > 1:

        argv = sys.argv[1:]

        try:
            opts, args = getopt.getopt(argv, "t:l:")
        except:
            print("Error!")

        # Get CLI arguments.
        file, text = None, None
        for opt, arg in opts:

            if opt in ['-t', '--text']:
                text = arg
            elif opt in ['-f', '--file']:
                file = arg
            elif opt in ['-l', '--language']:
                config.lang = arg

        # Check if language is supported and attempt to load embeddings.
        if config.lang in config.supported_langs:
            models.embeddings = models.load_embeddings(config.lang)

            # Simplify file or text depending on args.
            if file:
                with open(file) as f:
                    original_text = str(f.readlines()[0])
            elif text:
                original_text = text

            simple_text = simplifier.simplify_text(original_text.rstrip("\n"))
            print(simple_text)
            
        else:
            print("\nCannot simplify. Unsupported language entered.")
            print("\nSupported languages: " + str(config.supported_langs))

    else:

        models.embeddings = models.load_embeddings(config.lang)
        print("\nMiLeS Simplifier (type 'exit' to quit).")

        running = True
        while running:
            original_text = input("\nSimplifier Input: ")
            if original_text != "exit":
                simple_text = simplifier.simplify_text(original_text.rstrip("\n"))
                print("\n" + simple_text)
            else:
                running = False
