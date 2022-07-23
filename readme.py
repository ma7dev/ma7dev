from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🙂 [link=https://sudomaze.dev]Mazen Alotaibi", guide_style="bold bright_black")

python_tree = tree.add("📦 Open Source Packages", guide_style="bright_black")
python_tree.add("[bold link=https://github.com/approx-ml/approx]approx[/]       - [bright_black]automatic quantization library")
python_tree.add("[bold link=https://github.com/sudomaze/onlysudo]onlysudo[/]    - [bright_black]Discord/Twitch bot that uses AI models to do some cool stuff")

contrib_tree = tree.add("🔬 Experiments", guide_style="bright_black")
contrib_tree.add("[bold link=https://github.com/sudomaze/custom_dataset]custom_dataset[/]         - [bright_black]PyTorch dataset example for custom dataset")
contrib_tree.add("[bold link=https://github.com/sudomaze/automate-experiments]automate-experiments[/]           - [bright_black]automate experiments using GitHub Actions")
contrib_tree.add("[bold link=https://github.com/sudomaze/dvcorg-mlops]dvcorg-mlops[/]           - [bright_black]automate experiments using DVC")
contrib_tree.add("[bold link=https://github.com/sudomaze/ttorch]ttorch[/]         - [bright_black]a simple wrapper for PyTorch")
contrib_tree.add("[bold link=https://github.com/sudomaze/benthos-example]benthos-example[/]      - [bright_black]a simple example of using Benthos")
contrib_tree.add("[bold link=https://github.com/sudomaze/cookiecutter-pytorch-lightning]cookiecutter-pytorch-lightning[/]        - [bright_black]cookiecutter PyTorch Lightning")
contrib_tree.add("[bold link=https://github.com/sudomaze/cookiecutter-pytorch-lightning-cluster]cookiecutter-pytorch-lightning-cluster[/]   - [bright_black]cookiecutter PyTorch Lightning for cluster")
contrib_tree.add("[bold link=https://github.com/sudomaze/when-my-internet-is-down]when-my-internet-is-down[/]     - [bright_black]script to log when your interet is down")
contrib_tree.add("[bold link=https://github.com/sudomaze/LaTeX-Templates]LaTeX-Templates[/]     - [bright_black]a collection of LaTeX templates")

contrib_tree = tree.add("👍 Contributions", guide_style="bright_black")
contrib_tree.add("[bold link=https://github.com/pytorch/serve/pulls?q=sudomaze]pytorch/serve[/]      - [bright_black]contributed by adding `pre-commit`")
contrib_tree.add("[bold link=https://github.com/pytorch/examples/pulls?q=sudomaze]pytorch/examples[/]      - [bright_black]contributed by adding examples")
contrib_tree.add("[bold link=https://github.com/ARBML/klaam/pulls?q=sudomaze]ARBML/klaam[/]      - [bright_black]contributed by improving codebase and adding features")
contrib_tree.add("[bold link=https://github.com/ARBML/masader/pulls?q=sudomaze]ARBML/masader[/]      - [bright_black]contributed by improving website and adding features")
# contrib_tree.add("[bold link=https://github.com/HomebrewNLP/HomebrewNLP-Jax/pulls?q=sudomaze]HomebrewNLP-Jax[/]      - [bright_black]contributed by adding MLOps to automate experiments")

online_tree = tree.add("⭐ Online Projects", guide_style="bright_black")
online_tree.add("[bold link=https://sudomaze.dev]sudomaze.dev[/]     - [bright_black]personal blog")

employer_tree = tree.add("👨‍💻 Employer", guide_style="bright_black")

explosion_tree = employer_tree.add("[bold link=https://oregonstate.edu/]Oregon State University[/]  - [bright_black]developer tools for ml")
explosion_tree.add("[bold]Graduate Research Assistant[/]          - [bright_black]part of the computer vision team on Machine Common Sense project")
explosion_tree.add("[bold]Graduate Lead Teaching Assistant[/]      - [bright_black]undergard-level programming course")
explosion_tree.add("[bold]Graduate Teaching Assistant[/]      - [bright_black]undergard-level CS-core courses")

rasa_tree = employer_tree.add("[bold link=https://cqls.oregonstate.edu/]Center for Quantitative Life Sciences[/]       - [bright_black]conversational software")
rasa_tree.add("[bold]Computational Data Scientist[/]      - [bright_black]built a labeling tool, trained models end-to-end for different tasks (vision, sound, social interaction), and deployed them")
rasa_tree.add("[bold]Undergrad Lead GPU Researcher[/]             - [bright_black]led a team of 5 undergrad on different GPU research projects")
rasa_tree.add("[bold]Undergrad GPU Researcher[/]  - [bright_black]trained models and developed an web demo for IBM that was sponsored by the NVIDIA and AMD")

console.print(tree)
console.print("")
console.print("[green]Follow me on twitter [bold link=https://twitter.com/sudomaze]@sudomaze[/]")
console.print("[green]Follow me on twitch [bold link=https://twitch.tv/sudomaze]ttv/sudomaze[/]")
console.print("[green]Connect with me on linkedin [bold link=https://linkedin.com/in/sudomaze]Mazen Alotaibi[/]")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
