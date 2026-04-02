"use client";

import { useEffect, useState, ChangeEvent } from "react";

export default function TextInput() {
    // Declare a state variable for the input value
    const [value, setValue] = useState<string>('');

    // Event handler to update the state as the user types
    const handleChange = (event: ChangeEvent<HTMLInputElement>): void => {
        setValue(event.target.value);
    };

    return (
        <label className="flex flex-col w-md mx-auto content-center text-center text-lg">
            Reading: 
            <input
                type="text"
                value={value}
                onChange={handleChange}
                className="border-2 rounded-md text-lg text-center dark:border-mist-600 dark:hover:bg-mist-800 dark:focus:bg-mist-800"
            />
        </label>
    );
}