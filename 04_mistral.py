"""
Story Generation using Mistral AI (mistral-large-latest, mistral-small-latest)
Author: Deepak Kumar Chauhan (240330)
Assignment 6 | CS Assignment | IIT Kanpur

Requirements:
    pip install mistralai
    Set env var: MISTRAL_API_KEY=<your_key>
    Get key at: https://console.mistral.ai/api-keys/
"""

import os
import json
from mistralai import Mistral

# ─────────────────────────────────────────
#   GPT-4.1 Captions (used as input)
# ─────────────────────────────────────────
CAPTIONS = {
    "image_1": "Two young brothers engage in a fierce tug-of-war over a bright red toy airplane in their cozy living room. The older boy in a green tank top and blue shorts grips one wing tightly, his face set with stubborn determination, while his younger brother in an orange shirt and green shorts pulls from the other side. Their mother stands at the kitchen sink in the background, washing dishes and completely unaware of the brewing conflict behind her. The room has a warm, homey atmosphere with a pink-curtained window.",
    "image_2": "The red toy airplane now lies broken on the floor, its wings snapped off from the brothers' aggressive struggle. The younger boy sits on the floor, his face buried in his hands, sobbing uncontrollably over the destruction of the beloved toy. The older brother stands nearby looking shocked and guilty, clearly regretting his role in the toy's destruction. Their mother has turned from the sink, hands on hips, with an expression of exasperation and mild anger as she surveys the damage.",
    "image_3": "The two brothers now sit together peacefully at a round table, transformed from adversaries to collaborators. They are surrounded by colorful sheets of construction paper - red, yellow, and purple. The older brother in a green sleeveless shirt with a white star is carefully demonstrating the art of paper airplane folding to his younger sibling in an orange t-shirt, who watches with wide-eyed fascination and newfound enthusiasm. Several completed paper airplanes are already scattered across the table.",
    "image_4": "The living room has been transformed into a joyful paper airplane launch zone. Both brothers are laughing delightedly as they send their colorful paper creations soaring through the air. The older boy in his green shirt and blue shorts has just released a bright red paper airplane with perfect form, while his younger brother in orange watches its flight path with gleeful anticipation. Their mother stands at the room entrance smiling warmly, witnessing how her sons have turned conflict into creative collaboration."
}

STORY_PROMPT = f"""
You are a creative children's story writer. Based on the following image captions from a 4-image sequence, 
write a complete, engaging, and heartwarming children's story.

Image Captions:
{json.dumps(CAPTIONS, indent=2)}

Requirements:
- Length: 400-600 words
- Tone: Warm, family-friendly, with a clear moral lesson
- Name the characters (do not use Image 1, Image 2, etc.)
- The story must flow naturally across all 4 scenes
- End with a lesson about sharing, forgiveness, or creativity
- Write in third person narrative style
"""

MISTRAL_MODELS = {
    "mistral-large-latest":  "Mistral-Large",
    "mistral-small-latest":  "Mistral-Small",
    "open-mistral-nemo":     "Mistral-Nemo (Free)",
}


def generate_story(model_id: str, model_label: str, client: Mistral) -> str:
    """Generate a story using a Mistral model."""
    print(f"\n{'='*60}")
    print(f"Generating story with: {model_label}  [{model_id}]")
    print('='*60)

    response = client.chat.complete(
        model=model_id,
        messages=[
            {"role": "system", "content": "You are a creative and empathetic children's story writer. Write only the story, no preamble."},
            {"role": "user", "content": STORY_PROMPT}
        ],
        temperature=0.8,
        max_tokens=1000,
    )

    story = response.choices[0].message.content
    tokens = response.usage.total_tokens
    print(f"✓ Story generated | Tokens used: {tokens} | Words: {len(story.split())}")
    return story


def main():
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY not set. Get one at https://console.mistral.ai/api-keys/")

    client = Mistral(api_key=api_key)

    results = {}
    for model_id, model_label in MISTRAL_MODELS.items():
        try:
            story = generate_story(model_id, model_label, client)
            results[model_label] = story

            fname = model_label.lower().replace(".", "_").replace("-", "_").replace(" ", "_").replace("(", "").replace(")", "")
            with open(f"stories/{fname}.txt", "w") as f:
                f.write(f"Model: {model_label}\n")
                f.write("="*60 + "\n\n")
                f.write(story)
            print(f"✓ Saved: stories/{fname}.txt")

        except Exception as e:
            print(f"✗ Failed for {model_label}: {e}")
            results[model_label] = f"ERROR: {e}"

    with open("stories/mistral_stories.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\n✓ All Mistral stories saved to stories/mistral_stories.json")
    return results


if __name__ == "__main__":
    stories = main()
    for model, story in stories.items():
        print(f"\n{'─'*60}")
        print(f"  {model}")
        print('─'*60)
        print(story[:300] + "..." if len(story) > 300 else story)
