// https://www.reddit.com/r/dailyprogrammer/comments/3s4nyq/20151109_challenge_240_easy_typoglycemia/

extern crate rand;
extern crate unicode_segmentation;

use rand::Rng;
use unicode_segmentation::UnicodeSegmentation;

fn main() {
    let text = "Hello, world! What are you doing today?";
    println!("Before: {}", text);
    let shuffled_text = typoglycemia(&text);
    println!("After: {}", shuffled_text);
}

/// A scrambled form of the same sentence but with the words first and last letters positions intact.
fn typoglycemia(text: &str) -> String {
    let mut shuffled_text = String::new();
    let words: Vec<&str> = text.split(' ').collect();
    for word in &words {
        shuffle_word(&mut shuffled_text, &word)
    }
    shuffled_text
}
/// Shuffle letters of word but leave first and last letters positions intact.
fn shuffle_word(shuffled_text: &mut String, word: &str) {
    let mut letters = UnicodeSegmentation::graphemes(word, true).collect::<Vec<&str>>();
    let length = letters.len() - 1;
    rand::thread_rng().shuffle(&mut letters[1..length]);
    build_shuffled_text(shuffled_text, letters);
}

fn build_shuffled_text(shuffled_text: &mut String, letters: Vec<&str>) {
    for letter in &letters {
         shuffled_text.push_str(letter);
    }
    shuffled_text.push_str(" ");
}
