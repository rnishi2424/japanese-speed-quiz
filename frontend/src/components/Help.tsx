export default function Help() {
    return (
        <div className="fixed top-1/4 right-1/8 w-1/8 h-1/2 z-50 border-l-2 border-mist-600">
            <div className="flex h-full mx-auto px-4 sm:px-6 lg:px-8">
                <div className="justify-center hidden md:flex flex-col gap-y-8">
                    <p className="text-md">Type out the reading in Hiragana</p>
                    <p className="text-md">Click/Tap on blurred section to reveal more info</p>
                    <p className="text-md">Reveal Info:<br/> Ctrl + 1</p>
                </div>
            </div>
        </div>
    )
}