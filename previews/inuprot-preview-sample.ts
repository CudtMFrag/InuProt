// ============================================================================
//  InuProt preview sample — exercises the green-vs-orange contrast this theme
//  is tuned for. Open this file in VS Code with InuProt Dark / Light active,
//  then screenshot the editor for the repo previews.
// ============================================================================

// 1. Comments — should be muted gray italic (#888888 on dark).
//    (Not green, not orange — sits clearly apart from both.)

/* Block comment — same color, same italic. */

// 2. Keywords + declarations — INK GREEN (the "keyword green" of InuProt).
import { useState } from "react";
export const VERSION = "1.0.0";
let count: number = 0;
const threshold = 100;

// 3. Control flow + strings + numbers — ORANGE.
//    This is the color the greens above were dimmed to separate from.
if (count >= threshold) {
  try {
    throw new Error("max reached");
  } catch (error) {
    return null;
  }
}

// 4. Function calls — FUNCTION GREEN (one shade darker than keyword green).
function add(a: number, b: number): number {
  return a + b;
}
add(1, 2);

// 5. Types / classes — TEAL. Sits between green and orange on the wheel but
//    at a different luminance, so it's distinguishable for red-weak readers.
interface User {
  id: number;
  name: string;
  readonly email: string;
}

class Person implements User {
  constructor(public id: number, public name: string) {}
  greet(prefix: string = "Hi"): string {
    return `${prefix} ${this.name}`;
  }
}

// 6. Decorators + modifiers — RED. The accent that says "this is special".
@Component({ selector: "app" })
class AppComponent {}

// 7. Numbers and boolean constants — orange + dark-amber.
const num = 42;
const big = 1_000_000n;
const flag = true;
const nothing = null;

// 8. Template string with interpolation — string body orange, ${} interpolation
//    carries the variable color.
const tmpl = `count: ${count}, version: ${VERSION}`;

// 9. Regex — red-ish, so it reads as "different kind of string".
const re = /^[A-Z]\w+@example\.com$/gi;

// 10. Operators — light teal/cyan, sits apart from both green and orange.
const sum = a + b * c - d / e % f;
const cmp = a > b && c < d || e === f;