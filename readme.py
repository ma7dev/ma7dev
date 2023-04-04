from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🙂 [link=https://ma7.dev]Mazen Alotaibi", guide_style="bold bright_black")

python_tree = tree.add("📦 Open Source Packages", guide_style="bright_black")
python_tree.add("[bold link=https://github.com/approx-ml/approx]approx[/] \t\t - [bright_black]automatic quantization library")
python_tree.add("[bold link=https://github.com/ma7dev/onlysudo]onlysudo[/] \t - [bright_black]Discord/Twitch bot that uses AI models")
python_tree.add("[bold link=https://github.com/ma7dev/pyreqpp]pyreqpp[/] \t - [bright_black]automatic update missing module versions in requirements.txt to latest.")

contrib_tree = tree.add("🔬 Experiments", guide_style="bright_black")
contrib_tree.add("[bold link=https://github.com/ma7dev/deep-learning-project-template]deep-learning-project-template[/] \t\t - [bright_black]PyTorch Lightning, Pydantic, and more!")
contrib_tree.add("[bold link=https://github.com/ma7dev/custom_dataset]custom_dataset[/] \t\t\t\t - [bright_black]PyTorch dataset example for custom dataset")
contrib_tree.add("[bold link=https://github.com/ma7dev/automate-experiments]automate-experiments[/] \t\t\t - [bright_black]automate experiments using GitHub Actions")
contrib_tree.add("[bold link=https://github.com/ma7dev/dvcorg-mlops]dvcorg-mlops[/] \t\t\t\t - [bright_black]automate experiments using DVC")
contrib_tree.add("[bold link=https://github.com/ma7dev/ttorch]ttorch[/] \t\t\t\t\t - [bright_black]a simple wrapper for PyTorch")
contrib_tree.add("[bold link=https://github.com/ma7dev/benthos-example]benthos-example[/] \t\t\t - [bright_black]a simple example of using Benthos")
contrib_tree.add("[bold link=https://github.com/ma7dev/cookiecutter-pytorch-lightning]cookiecutter-pytorch-lightning[/] \t\t - [bright_black]cookiecutter PyTorch Lightning")
contrib_tree.add("[bold link=https://github.com/ma7dev/cookiecutter-pytorch-lightning-cluster]cookiecutter-pytorch-lightning-cluster[/] \t - [bright_black]cookiecutter PyTorch Lightning for cluster")
contrib_tree.add("[bold link=https://github.com/ma7dev/when-my-internet-is-down]when-my-internet-is-down[/] \t\t - [bright_black]script to log when your interet is down")
contrib_tree.add("[bold link=https://github.com/ma7dev/LaTeX-Templates]LaTeX-Templates[/] \t\t\t - [bright_black]a collection of LaTeX templates")

contrib_tree = tree.add("👍 Contributions", guide_style="bright_black")
contrib_tree.add("[bold link=https://github.com/pytorch/serve/pulls?q=ma7dev]pytorch/serve[/] \t\t - [bright_black]contributed by adding features")
contrib_tree.add("[bold link=https://github.com/pytorch/examples/pulls?q=ma7dev]pytorch/examples[/] \t - [bright_black]contributed by adding examples")
# contrib_tree.add("[bold link=https://github.com/HomebrewNLP/HomebrewNLP-Jax/pulls?q=ma7dev]HomebrewNLP-Jax[/] \t - [bright_black]contributed by adding MLOps to automate experiments")

online_tree = tree.add("⭐ Online Projects", guide_style="bright_black")
online_tree.add("[bold link=https://ma7.dev]ma7.dev[/] \t - [bright_black]personal blog")

employer_tree = tree.add("👨‍💻 Employer", guide_style="bright_black")

explosion_tree = employer_tree.add("[bold link=https://oregonstate.edu/]Oregon State University[/] \t\t - [bright_black]Faculty Research Assistant")
explosion_tree.add("[bold]Machine Common Sense[/] \t\t\t - [bright_black]part of the CV team and core-maintainer")

explosion_tree = employer_tree.add("[bold link=https://oregonstate.edu/]Oregon State University[/] \t\t - [bright_black]Graduate Research/Teaching Assistant")
explosion_tree.add("[bold]Machine Common Sense[/] \t\t\t - [bright_black]part of the CV team and core-maintainer")
explosion_tree.add("[bold]Undergard-level programming course[/] \t - [bright_black]led a team of 4 undergrad TAs")
explosion_tree.add("[bold]Undergard-level CS-core courses[/] \t - [bright_black]taught 5 courses in the CS department")

rasa_tree = employer_tree.add("[bold link=https://cqls.oregonstate.edu/]Center for Quantitative Life Sciences[/]       - [bright_black]Data Scientist and Undergrad Lead Researcher")
rasa_tree.add("[bold]How long was the poultry sick?[/] \t - [bright_black]classifying poultry diseases from sound data")
rasa_tree.add("[bold]Measuring interaction in sport[/] \t - [bright_black]how players interact with each others")
rasa_tree.add("[bold]Labeling tool[/] \t\t\t - [bright_black]labeling images for object detection tasks")
rasa_tree.add("[bold]Plankton Detection[/] \t\t - [bright_black]detecting plankton from imagery data")
rasa_tree.add("[bold]Owl Sound Classification[/] \t - [bright_black]classifying owl type from sound data")
rasa_tree.add("[bold]AI Web Demo[/] \t\t\t - [bright_black]sponsored by TechData, IBM, NVIDIA, and AMD")

console.print(tree)
console.rule("[bold red]Socials")
console.print("[green]Connect with me on linkedin [bold link=https://linkedin.com/in/ma7dev]Mazen Alotaibi[/].")
# line
console.rule("[bold red]Thanks")
console.print("[yellow]This is a fork from [bold link=https://github.com/koaning/koaning]Vincent D. Warmerdam (koaning)[/].")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
