// This file contains a reusable Button component for the UI library. It defines the button's appearance and behavior, allowing for consistent styling across the application.


import * as React from "react";
import { cn } from "../../lib/utils";

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement> {}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, ...props }, ref) => {
    return (
      <button
        ref={ref}
        className={cn(
          "px-4 py-2 rounded-md bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50",
          className
        )}
        {...props}
      />
    );
  }
);

Button.displayName = "Button";
