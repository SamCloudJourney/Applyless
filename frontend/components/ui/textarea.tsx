import * as React from "react";
import { cn } from "../../lib/utils";

const Textarea = React.forwardRef<HTMLTextAreaElement, React.TextareaHTMLAttributes<HTMLTextAreaElement>>(
  ({ className, ...props }, ref) => (
    <textarea
      className={cn(
        "flex min-h-[120px] w-full rounded-md border border-slate-200 bg-white px-3 py-2 text-sm focus-visible:outline-brand",
        className
      )}
      ref={ref}
      {...props}
    />
  )
);

export { Textarea };
