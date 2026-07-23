<div align="center">

# Practical Problem Solving

From Computational Thinking to Programs with Python.

<a href="docs/en/Practical-Problem-Solving.pdf">
   <img src="https://github.com/igorbenav/problem-solving-with-python/blob/main/en/images/cover.png" width="30%" alt="Book Cover">
</a>

An open book that teaches programming by starting with problems. Every concept exists because a problem demands it, not because it's the next item in a language tour. Opinionated, hands-on, and meant to be read in order. Each chapter builds on the previous one.

No prior programming experience needed.

**[Read the English version (PDF)](docs/en/Practical-Problem-Solving.pdf)**

</div>

---

The book follows a single thread: a receipt printer that starts simple and grows more capable as you learn new concepts. Each chapter solves the previous chapter's limitation and reveals the next one. Concepts like algorithms, abstraction, and decomposition are introduced when the problem at hand requires them.

## Table of Contents

| Chapter | Topic |
|:-------:|-------|
| 1 | The Foundations of Computational Thinking |
| 2 | Getting Started with Python |
| 3 | Types, Conversions, and Formatting |
| 4 | Making Decisions |

More chapters will be added.

## Available Languages

| Language | Directory | Status |
|:--------:|:---------:|:------:|
| English | [en/](en/) | In progress |

## Getting Started

### Prerequisites

- [Python 3.11+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) - Python package manager
- [Quarto](https://quarto.org/docs/get-started/) - Publishing system

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/igorbenav/problem-solving-with-python.git
   cd problem-solving-with-python
   ```

2. Install Python dependencies with uv:
   ```bash
   uv sync
   ```

## Building the Book

| Format | Command | Output |
|--------|---------|--------|
| HTML (default) | `uv run quarto render en/` | `docs/en/index.html` |
| PDF | `uv run quarto render en/ --to pdf` | `docs/en/` |
| Preview with live reload | `uv run quarto preview en/` | localhost |

> Note: PDF rendering requires a LaTeX distribution (e.g., [TinyTeX](https://yihui.org/tinytex/), [TeX Live](https://www.tug.org/texlive/), or [MiKTeX](https://miktex.org/)).

## Project Structure

```
problem-solving-with-python/
├── en/                          # English
│   ├── _quarto.yml
│   ├── index.qmd
│   ├── references.qmd
│   ├── references.bib
│   ├── chapters/
│   │   ├── chapter1.qmd
│   │   ├── chapter2.qmd
│   │   ├── chapter3.qmd
│   │   └── chapter4.qmd
│   ├── images/                  # Figures (language-specific)
│   │   ├── chapter1/
│   │   ├── chapter2/
│   │   ├── chapter3/
│   │   └── chapter4/
│   └── code/                    # Completed code per chapter
│       └── chapter1/
├── docs/                        # Rendered output
│   └── en/
├── README.md
├── LICENSE
├── pyproject.toml
└── .gitignore
```

## Adding a New Language

To translate the book into a new language:

1. Copy the `en/` directory as your starting point:
   ```bash
   cp -r en/ pt-br/   # for Brazilian Portuguese, for example
   ```

2. In your new directory (e.g., `pt-br/`):
   - Translate all `.qmd` files (chapters, index, references)
   - Translate or recreate images that contain text (SVGs in `images/`)
   - Update `_quarto.yml`: change `output-dir` to `../docs/pt-br` and translate the title/subtitle
   - Code in `code/` may need translated comments

   Each language builds into its own `docs/` directory, so the PDF is simply named in that language. The filename comes from the book `title` you set in `_quarto.yml` - translating the title is all you need, no extra setting. A title of `"Resolução de Problemas na Prática com Python"` produces `docs/pt-br/Resolução-de-Problemas-na-Prática-com-Python.pdf`.

3. Update the cover image:
   - Edit `images/cover.svg` translate the text elements (title, subtitle, author) to your language
   - Convert the SVG to PNG for PDF rendering (requires `rsvg-convert`, installed via `librsvg`):
     ```bash
     rsvg-convert -f png -w 2550 -h 3300 -o pt-br/images/cover.png pt-br/images/cover.svg
     ```

4. Build with:
   ```bash
   uv run quarto render pt-br/
   uv run quarto render pt-br/ --to pdf
   ```

5. Add yourself to the contributors table below and submit a pull request.

## Contributors

| Name | GitHub | Role | Language |
|------|--------|------|----------|
| Igor Benav | [@igorbenav](https://github.com/igorbenav) | Author | English |

When your translation or review is merged, add yourself in the same pull request to:

1. The **Contributors** table above (this README)
2. The **Contributors** table in your language's `index.qmd` (this appears in the actual book)

Roles: "Translator", "Reviewer", or both.

## Citation

```bibtex
@book{benav2026practical-problem-solving,
  title     = {Practical Problem Solving: From Computational Thinking to Programs with Python},
  author    = {Igor Benav},
  year      = {2026},
  url       = {https://github.com/igorbenav/problem-solving-with-python}
}
```

## License

MIT License - see [LICENSE](LICENSE) for details.
