# <div align="center">Assignment 6 — Image Captioning & Story Generation</div>

<div align="center">

### 👤 Deepak Kumar Chauhan &nbsp;|&nbsp; Roll No. `240330` &nbsp;|&nbsp; IIT Kanpur


</div>

---

## Objective

> Explore multiple **image captioning models** and use their output to generate coherent, heartwarming **children's stories** via state-of-the-art LLMs.

---

## Dataset

4 static illustrations depicting two brothers and their mother in a conflict-resolution arc:

| # | Scene Description |
|---|-------------------|
| 1 | Brothers fight over a red toy airplane; mother unaware at the sink |
| 2 | Airplane breaks; younger brother cries; mother is angry |
| 3 | Brothers sit together and fold paper airplanes cooperatively |
| 4 | Both brothers laugh and fly paper airplanes; mother smiles |

> **Images fetched via `requests` and processed with `PIL`.**

---

## Part 1 — Image Captioning

### Models Explored

| Model | Pros | Cons |
|-------|------|------|
| **Salesforce BLIP** | Lightweight, fast inference | Less detail than BLIP-2 |
| **Salesforce BLIP-2 (OPT 2.7B)** | Accurate, summarized descriptions | Heavy memory usage |
| **ViT-GPT2** | Very lightweight | Poor contextual understanding |
| **Kosmos-2** | Good at activity detection | Over-interprets scenes |
| **Florence-2 Flux Large** | Balanced identification + detail | Large model, limited emotional context |
| **GIT Large TextCaps** | Excellent object + room recognition | Occasional scene misinterpretation |
| **GPT-4.1**  | Extremely detailed, best storytelling | Requires API key (cost incurred) |

>  **Final captions used for story generation are from GPT-4.1** — most accurate and contextually rich.

---

##  Part 2 — Story Generation

### LLMs Used

| # | Model | Provider | Script | Story |
|---|-------|----------|--------|-------|
| 1 | **GPT-4o** | OpenAI | `01_openai_gpt4.py` | [Jump ↓](#gpt-4o) |
| 2 | **GPT-4o-mini** | OpenAI | `01_openai_gpt4.py` | [Jump ↓](#gpt-4o-mini) |
| 3 | **Gemini-2.0-Flash** | Google | `02_gemini.py` | [Jump ↓](#gemini-20-flash) |
| 4 | **Gemini-1.5-Pro** | Google | `02_gemini.py` | [Jump ↓](#gemini-15-pro) |
| 5 | **Llama3-8B** | Groq | `03_groq_models.py` | [Jump ↓](#llama3-8b) |
| 6 | **Llama3.3-70B** | Groq | `03_groq_models.py` | [Jump ↓](#llama33-70b) |
| 7 | **Gemma2-9B** | Groq | `03_groq_models.py` | [Jump ↓](#gemma2-9b) |
| 8 | **DeepSeek-R1** | Groq | `03_groq_models.py` | [Jump ↓](#deepseek-r1) |
| 9 | **Mistral-Large** | Mistral AI | `04_mistral.py` | [Jump ↓](#mistral-large) |
| 10 | **Mistral-Nemo** | Mistral AI | `04_mistral.py` | [Jump ↓](#mistral-nemo) |
| 11 | **Claude-3.5-Sonnet** | Anthropic | `05_claude_anthropic.py` | [Jump ↓](#claude-35-sonnet) |
| 12 | **Claude-3-Haiku** | Anthropic | `05_claude_anthropic.py` | [Jump ↓](#claude-3-haiku) |

---

##  Setup & Execution

### 1. Install Dependencies

```bash
pip install openai google-generativeai groq mistralai anthropic
```

### 2. Set API Keys

```bash
export OPENAI_API_KEY="sk-..."
export GEMINI_API_KEY="AIza..."
export GROQ_API_KEY="gsk_..."
export MISTRAL_API_KEY="..."
export ANTHROPIC_API_KEY="sk-ant-..."
```

### 3. Run Scripts

```bash
# OpenAI GPT-4o & GPT-4o-mini
python scripts/01_openai_gpt4.py

# Google Gemini-2.0-Flash & Gemini-1.5-Pro
python scripts/02_gemini.py

# Groq: Llama3, Gemma2, DeepSeek-R1, Mistral-Saba (ALL FREE)
python scripts/03_groq_models.py

# Mistral AI: Large, Small, Nemo
python scripts/04_mistral.py

# Anthropic Claude: 3.5-Sonnet & Haiku
python scripts/05_claude_anthropic.py
```

>  **Stories are saved as `.txt` and `.json` in the `stories/` folder.**

---

##  Model Comparison Summary

| Model | Provider | Cost | Quality | Speed | Best For |
|-------|----------|------|---------|-------|----------|
| GPT-4o | OpenAI | 💰💰 | ⭐⭐⭐⭐⭐ | Medium | Best overall quality |
| GPT-4o-mini | OpenAI | 💰 | ⭐⭐⭐⭐ | Fast | Budget-friendly, still strong |
| Gemini-2.0-Flash | Google | 💰 | ⭐⭐⭐⭐ | Very Fast | Speed + quality balance |
| Gemini-1.5-Pro | Google | 💰💰 | ⭐⭐⭐⭐⭐ | Medium | Long context, detailed |
| Llama3-8B | Groq | 🆓 | ⭐⭐⭐ | Very Fast | Free, good baseline |
| Llama3.3-70B | Groq | 🆓 | ⭐⭐⭐⭐ | Fast | Free, near-GPT-4 quality |
| Gemma2-9B | Groq | 🆓 | ⭐⭐⭐ | Very Fast | Free, Google-trained |
| DeepSeek-R1 | Groq | 🆓 | ⭐⭐⭐⭐ | Medium | Free, reasoning-heavy |
| Mistral-Large | Mistral AI | 💰💰 | ⭐⭐⭐⭐ | Fast | EU-based, strong multilingual |
| Mistral-Nemo | Mistral AI | 🆓 | ⭐⭐⭐ | Very Fast | Free, compact |
| Claude-3.5-Sonnet | Anthropic | 💰💰 | ⭐⭐⭐⭐⭐ | Medium | Best narrative quality |
| Claude-3-Haiku | Anthropic | 💰 | ⭐⭐⭐⭐ | Very Fast | Fast, cost-efficient |

---

##  Stories Generated

---

### GPT-4o

> *[Paste story here after running `01_openai_gpt4.py`]*

<details>
<summary>📖 Click to expand full story</summary>

<!-- PASTE GPT-4o STORY HERE -->

</details>

---

### GPT-4o-mini

> *[Paste story here after running `01_openai_gpt4.py`]*

<details>
<summary>📖 Click to expand full story</summary>

<!-- PASTE GPT-4o-mini STORY HERE -->

</details>

---

### Gemini-2.0-Flash

> *[Paste story here after running `02_gemini.py`]*

<details>
<summary>📖 Click to expand full story</summary>

<!-- PASTE GEMINI-2.0-FLASH STORY HERE -->

</details>

---

### Gemini-1.5-Pro

> *[Paste story here after running `02_gemini.py`]*

<details>
<summary>📖 Click to expand full story</summary>

<!-- PASTE GEMINI-1.5-PRO STORY HERE -->

</details>

---

### Llama3-8B

> *[Paste story here after running `03_groq_models.py`]*

<details>
<summary>📖 Click to expand full story</summary>

<!-- PASTE LLAMA3-8B STORY HERE -->

</details>

---

### Llama3.3-70B

> *[Paste story here after running `03_groq_models.py`]*

<details>
<summary>📖 Click to expand full story</summary>

<!-- PASTE LLAMA3.3-70B STORY HERE -->

</details>

---

### Gemma2-9B

> *[Paste story here after running `03_groq_models.py`]*

<details>
<summary>📖 Click to expand full story</summary>

<!-- PASTE GEMMA2-9B STORY HERE -->

</details>

---

### DeepSeek-R1

> *[Paste story here after running `03_groq_models.py`]*

<details>
<summary>📖 Click to expand full story</summary>

<!-- PASTE DEEPSEEK-R1 STORY HERE -->

</details>

---

### Mistral-Large

> *[Paste story here after running `04_mistral.py`]*

<details>
<summary>📖 Click to expand full story</summary>

<!-- PASTE MISTRAL-LARGE STORY HERE -->

</details>

---

### Mistral-Nemo

> *[Paste story here after running `04_mistral.py`]*

<details>
<summary>📖 Click to expand full story</summary>

<!-- PASTE MISTRAL-NEMO STORY HERE -->

</details>

---

### Claude-3.5-Sonnet

> *[Paste story here after running `05_claude_anthropic.py`]*

<details>
<summary>📖 Click to expand full story</summary>

<!-- PASTE CLAUDE-3.5-SONNET STORY HERE -->

</details>

---

### Claude-3-Haiku

> *[Paste story here after running `05_claude_anthropic.py`]*

<details>
<summary>📖 Click to expand full story</summary>

<!-- PASTE CLAUDE-3-HAIKU STORY HERE -->

</details>

---

## 📁 Repository Structure

```
Assignment6-240330/
│
├── 📄 README.md                       ← This file
│
├── 📂 scripts/
│   ├── 01_openai_gpt4.py              ← GPT-4o & GPT-4o-mini
│   ├── 02_gemini.py                   ← Gemini-2.0-Flash & 1.5-Pro
│   ├── 03_groq_models.py              ← Llama3, Gemma2, DeepSeek, Mistral (FREE)
│   ├── 04_mistral.py                  ← Mistral Large & Nemo
│   └── 05_claude_anthropic.py         ← Claude 3.5 Sonnet & Haiku
│
└── 📂 stories/
    ├── gpt_4o.txt
    ├── gpt_4o_mini.txt
    ├── gemini_2_0_flash.txt
    ├── gemini_1_5_pro.txt
    ├── llama3_8b.txt
    ├── llama3_3_70b.txt
    ├── gemma2_9b.txt
    ├── deepseek_r1.txt
    ├── mistral_large.txt
    ├── mistral_nemo.txt
    ├── claude_3_5_sonnet.txt
    ├── claude_3_haiku.txt
    ├── openai_stories.json
    ├── gemini_stories.json
    ├── groq_stories.json
    ├── mistral_stories.json
    └── claude_stories.json
```

---

<div align="center">

Made with ☕ by **Deepak Kumar Chauhan** &nbsp;|&nbsp; IIT Kanpur `240330`

</div>
