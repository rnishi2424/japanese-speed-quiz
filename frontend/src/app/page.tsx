import VocabCard from "../components/VocabCard"
import TextInput from "../components/TextInput"
import Help from "../components/Help"

export default function Home() {
  return (
    <div className="flex flex-1 w-full max-w-3xl flex-col items-center py-32 px-16 bg-white dark:bg-black sm:items-start">
      
      <div className="flex flex-col mx-auto my-auto">
        <VocabCard/>
        <TextInput/>
        <Help/>
      </div>

    </div>
  );
}
