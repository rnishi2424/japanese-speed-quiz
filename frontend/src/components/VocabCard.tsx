"use client";

import { useEffect, useState, useCallback } from "react";
import { getRandomVocab } from "../api/vocab";

type Vocab = {
  id: number;
  kanji: string;
  furigana: string | null;
  english: string | null;
  jlpt_level: number | null;
}

export default function VocabCard() {
  const [vocab, setVocab] = useState<Vocab | null>(null);
  const [isVisible, setIsVisible] = useState<boolean>(false);

  useEffect(() => {
    getRandomVocab().then((data: Vocab) => setVocab(data));
  }, []);

  const toggleReveal = useCallback(() => {
    setIsVisible((prev) => !prev);
  }, []);

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.ctrlKey && event.key === '1') {
        event.preventDefault();
        toggleReveal();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [toggleReveal]);

  if (!vocab) return <div>Loading...</div>;

  return (
    <div className="flex flex-col w-lg mb-16 mx-auto justify-center text-center relative p-2">
      <h1 className="text-4xl mb-4">{vocab.kanji}</h1>

      <div className="absolute top-0 right-8 border rounded-sm px-1">
        <h2>N{vocab.jlpt_level}</h2>
      </div>

      <div 
        onClick={toggleReveal}
        className={`cursor-pointer transition-all duration-200 rounded-lg ${
          isVisible ? "blur-none opacity-100" : "blur-sm opacity-50"
        }`}
      >
        <p className="text-xl">{vocab.furigana}</p>
        <p className="text-lg">{vocab.english}</p>
      </div>

    </div>
  );
}