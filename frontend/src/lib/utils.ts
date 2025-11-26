// This utility function combines multiple class names into a single string, filtering out any falsy values. It is useful for conditionally applying CSS classes in React components.

export function cn(...inputs: any[]) {
  return inputs.filter(Boolean).join(" ");
}
