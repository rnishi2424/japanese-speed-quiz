const API_BASE = "http://localhost:8000";

type Vocab = {
  id: number;
  kanji: string;
  furigana: string | null;
  english: string | null;
  jlpt_level: number | null;
};

export async function getRandomVocab(): Promise<Vocab> {
  const res = await fetch(`${API_BASE}/vocab/random`);

  if (!res.ok) {
    throw new Error("Failed to fetch vocab");
  }

  return res.json();
}