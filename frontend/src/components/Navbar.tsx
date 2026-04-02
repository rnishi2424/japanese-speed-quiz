"use client";

import { usePathname } from "next/navigation";
import Link from "next/link";

export default function Navbar() {
    const pathname = usePathname();

    const navLinks = [
    { name: "Home", href: "/" },
    { name: "Dashboard", href: "/dashboard" },
    { name: "Decks", href: "/decks" },
    { name: "Vocabulary", href: "/vocabulary" },
    ];

    return (
    <nav className="fixed top-1/4 left-1/8 w-1/8 h-1/2 z-50 border-r-2 border-mist-600">
        <div className="flex h-full mx-auto px-4 sm:px-6 lg:px-8">
            {/* Desktop Menu */}
            <div className="justify-center hidden md:flex flex-col gap-y-8 w-full">
                {navLinks.map((link) => {
                    const isActive = pathname === link.href;

                    return (
                        <Link
                        key={link.name}
                        href={link.href}
                        className={`transition-colors font-medium text-right text-2xl h-8 m-0 ${
                            isActive 
                            ? "text-emerald-400" // Active style
                            : "text-white hover:text-emerald-400" // Inactive style
                        }`}
                        >
                        {link.name}
                        </Link>
                    );
                })}
            </div>
        </div>
    </nav>
  );
}