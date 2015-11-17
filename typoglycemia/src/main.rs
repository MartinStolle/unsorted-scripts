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
    text.split(' ').map(shuffle_word).collect()
}

/// Shuffle letters of word but leave first and last letters positions intact.
fn shuffle_word(word: &str) -> String {
    let mut letters = UnicodeSegmentation::graphemes(word, true).collect::<Vec<&str>>();
    let length = letters.len() - 2;
    rand::thread_rng().shuffle(&mut letters[1..length]);
    letters.concat() + " "
}
