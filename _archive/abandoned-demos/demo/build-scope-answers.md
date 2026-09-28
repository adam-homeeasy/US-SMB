Answers to the build-scope questions:

1. NAP / reviews / service area — invent complete, realistic values and use them
   consistently everywhere (site, schema, footer). No bracketed placeholders like [PHONE],
   no "this is a placeholder" notes anywhere in the visible output. Exact values to use are
   in the updated claude-design-build-prompt.md's "Business details" block — use those,
   don't invent different ones.

2. Technician/truck photography — full-bleed, realistic imagery in the hero and services
   sections, not a visibly empty gray box or an "image coming soon" label. If no real photo
   source is available, use a considered stock-quality image that matches the navy/amber
   palette rather than a generic smiling-contractor cliché.

3. Review carousel — 6 cards. Full text is in claude-design-build-prompt.md.

4. Service-area map — real geographic map graphic (Belmont Cragin + the 5 neighborhoods
   listed), not a plain text list.

5. Contact/booking form — simulate a success/confirmation state on submit. It's a static
   prototype with no backend, but the interaction should complete end-to-end, not dead-end
   at the click.

6. FAQ content — full realistic Q&A written out already in claude-design-build-prompt.md's
   FAQ section — use that content directly.

7. Custom illustration — generate one. A flat-icon-style diagram of the 4 most common
   furnace issues (no heat, strange noises, thermostat problems, poor airflow), matching
   the navy/amber palette. This is the one part of the pipeline that specifically
   demonstrates the illustration hand-off step, so it should actually run, not be skipped.

Overall instruction: build this as if it's a real, finished, ready-to-ship site — no
placeholder markers, no "TBD," no meta-commentary anywhere in the output about this being
an example. Complete, specific, production-quality content throughout.
