# Claude’s Android redesign: go native on structure, keep your brand on the surface

> Anthropic rolled out a Material 3 Expressive redesign of the Claude Android app this week: a bottom navigation bar instead of a hamburger-first layout, Material components in the model switcher, and Anthropic’s own colours instead of wallpaper-based dynamic colour. We read it as a pattern for every AI product shipping a mobile app: borrow the platform’s navigation, back gesture and motion, keep your palette, type and one or two hero moments. What to adopt, what to keep, a checklist and a prompt for coding agents.

Blog post: <https://ui.incidental.site/blog/claude-android-native-shell-brand-surface/>

Anthropic is rolling out a redesigned Claude app for Android. Product manager Robert Bye announced it on X on 23 November: “we went full Material 3 Expressive to make everything feel as native as possible.” 9to5Google’s Ben Schoon, who looked at the build the same day, describes a bottom bar that replaces the old reliance on the hamburger menu (the menu stays, but now mostly holds chat history), Material 3 elements in the model switcher and the chat background, and colours that stay Anthropic’s own rather than following the phone’s wallpaper. Three days earlier Bye had introduced a new mobile app with a tab bar on both iOS and Android, so this is the Android-specific layer on top of a shared structure.

The reaction is what makes it worth a post. Matthew McCullough, thanking Anthropic on behalf of Android’s developer team, summed it up as “native navigation… and Material 3 Expressive motion, and it still feels like Claude.” That last clause is the design problem every AI product team has right now. Chat apps all share the same shell: a composer, a history list, a model picker, settings. The difference between them is the conversation, not the chrome. So the chrome can afford to behave like the platform, and the brand can live somewhere more useful.

## What actually changed

- **Navigation became visible.** Core destinations moved to a bottom navigation bar within thumb reach. Material 3 recommends a navigation bar for 3–5 destinations of equal importance on windows narrower than 840dp, and the Expressive update replaced the baseline bar with a shorter “flexible” one. Chat history, which is a long list rather than a destination, stays behind the menu.

- **Components came from the system.** The model switcher and chat surfaces use Material 3 components, so they inherit the platform’s states, shapes and spring-based motion instead of a custom imitation.

- **Colour stayed on brand.** 9to5Google saw no obvious use of Material You dynamic colour. Android supports this choice: its docs show how to keep brand colours fixed, and how to harmonise custom colours so they sit well next to user-generated palettes.

- **One rough edge.** The back gesture animates the search bar, but does not preview the previous screen the way Android’s predictive back guidance expects. 9to5Google called it nit-picking. We think it is the most useful detail in the story, because it is the part users feel without being able to name it.

## Our take: borrow the skeleton, keep the skin

For years many AI apps shipped one cross-platform design with a hamburger menu and a custom palette everywhere. It was cheap, and it hid the product’s structure. Nielsen Norman Group’s quantitative study of hidden navigation found that hiding the main navigation cut discoverability almost in half, and recommended showing up to four top-level links on phones. A bottom bar is the mobile answer to that, and Material 3 Expressive gives it to you with motion and states already tuned.

The split we would copy is simple. Anything the user’s hands and habits already know belongs to the platform: where navigation lives, how back works, how sheets open, how fast things spring. Anything that makes the product recognisable belongs to the brand: palette, typeface, illustration, the tone of the copy, and one or two hero moments. Google’s own Expressive guidance says the same about the last point: stick to one or two hero moments, because more becomes distracting. For an AI app the obvious candidate is the moment a response starts to stream.

Two cautions. First, “native” is a contract, not a style. If you adopt the platform’s look, people expect its behaviour, and a back gesture that does not preview, or a sheet that ignores gesture insets, feels more broken in a native-looking app than in an obviously custom one. Second, native per platform means iOS gets its own answer. Bye’s first announcement covered a tab bar on both systems; on iOS the reference is Apple’s tab bar guidance, not the Android bar ported across.

## Adopt or keep: a working split

- **Adopt the navigation model.** Count your top-level destinations. Three to five equal ones go in the bottom bar; long lists such as history go in a drawer, sheet or search.

- **Adopt back behaviour.** Opt in to predictive back. Since Android 15, the system back-to-home, cross-activity and cross-task animations appear for apps that opt in. For your own full-screen surfaces, Android’s spec scales the outgoing screen to 90% and fades through at 35% of the gesture.

- **Adopt motion tokens.** Use the Expressive spring tokens for components instead of hand-picked durations.

- **Keep your palette, deliberately.** Map brand colours to Material colour roles (primary, secondary, tertiary, surface containers) so components theme correctly, then decide on dynamic colour: off, or harmonised custom colours. Write the decision down.

- **Keep type and voice.** Use your typeface through the type scale roles, and keep your copy style in labels and empty states.

- **Keep one or two hero moments.** Put the brand’s motion and colour where it matters most, and leave everything else calm.

## Platform-fit checklist

- Do the 3–5 bottom-bar destinations stay the same on every screen, with long lists kept out of the bar?

- Does every back swipe preview where it goes, and does releasing early restore the screen exactly?

- Are no touch targets placed under the system gesture insets in edge-to-edge layouts?

- Are brand colours mapped to colour roles, checked for contrast in light and dark, with the dynamic-colour decision recorded?

- Do model pickers, menus and sheets use system components, so states and motion come for free?

- Is there at most one or two expressive hero moments, and is everything else quiet?

- Does the same check pass on iOS against its own conventions, rather than a port of the Android layout?

```
# Paste into a coding agent building an Android screen (Jetpack Compose)
Build <screen> with Material 3 Expressive components.
Navigation: bottom navigation bar with these 3–5 destinations: <list>.
Put long lists (history, files) in a drawer or search, not in the bar.
Back: enable predictive back; custom full-screen transitions scale to 90%
and fade through at 35% of gesture progress; releasing early restores state.
Colour: map our brand colours to colour roles (primary, secondary, tertiary,
surface containers). Dynamic colour: <off | harmonise custom colours>.
Type: our typeface via the Material type scale roles.
Motion: Expressive spring tokens only; one hero moment: <describe>.
Respect edge-to-edge gesture insets. Report light and dark screenshots
and a list of any component you had to build by hand.
```

Related on UI Hub: 
handing off physics-based springs
, 
gestures with fallbacks
, and 
designing for the platform’s adaptive dark mode
.

## References
- [For Android users, we went full Material 3 Expressive](https://x.com/RobertJBye/status/2124961333494124589) — Robert Bye · X
- [Meet the new Claude mobile app](https://x.com/RobertJBye/status/2123930535437504635) — Robert Bye · X
- [Native navigation and Material 3 Expressive motion, and it still feels like Claude](https://x.com/matthewmccull/status/2125372019583963610) — Matthew McCullough · X
- [Claude rolling out updated Android app with Material 3 Expressive redesign](https://9to5google.com/2026/11/23/claude-android-material-3-update/) — Ben Schoon · 9to5Google
- [Claude rolls out updated Android app with Material 3 Expressive design](https://www.macobserver.com/news/claude-rolls-out-updated-android-app-with-material-3-expressive-design/) — The Mac Observer
- [Start building with Material 3 Expressive](https://m3.material.io/blog/building-with-m3-expressive) — Material Design
- [Navigation bar](https://m3.material.io/components/navigation-bar/overview) — Material Design 3
- [Predictive back design](https://developer.android.com/design/ui/mobile/guides/patterns/predictive-back) — Android Developers
- [Add support for the predictive back gesture](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture) — Android Developers
- [Enable users to personalize their color experience in your app](https://developer.android.com/develop/ui/views/theming/dynamic-colors) — Android Developers
- [Hamburger Menus and Hidden Navigation Hurt UX Metrics](https://www.nngroup.com/articles/hamburger-menus/) — Kara Pernice, Raluca Budiu · Nielsen Norman Group
- [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) — Apple Human Interface Guidelines