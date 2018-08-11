const counterArr = (arr_to_count,word) =>{
  // Function to count the occurances of a word in an array of words
  // returns an array with [0] being the word and [1] being the count
  let setOfWords = arr_to_count.filter(target => target == word)
  return [word,setOfWords.length]
}
const counterObj = (arr_to_count,word) =>{
  // Function to count the occurances of a word in an array of words
  // returns an object {word: counts}
  let setOfWords = arr_to_count.filter(target => target == word)
  let counter ={}
  counter[`${word}`] = setOfWords.length
  return counter
}

// Helper Function

// class definitions
export class Histogram {
  constructor(file_path){
  this.file_path =file_path;
  }
  // Getter
  get path(){
    return this._file_path;
  }
  // end Getter

  // Setter
  set file_path(file_name){
    if(file_name.endsWith('.txt')){
      // console.log("Valid")
      this._file_path = file_name;
    }
    else{
      console.log("Not a valid .txt extention")
    }
  }
// end Setter

// Array Histogram
async arrayHistogram(){
  const file = await fetch(this._file_path);
  const fileText = await file.text()
  fileText.then
  const newlineCleaner =fileText.replace('\n',"");
  const periodCleaner = newlineCleaner.replace('.','');
  const commaCleaner = periodCleaner.replace(',','');
  const split = commaCleaner.split(' ');
  const arrayGram = [];
  split.forEach( word => arrayGram.push(counterArr(split,word)))
  for(let count of arrayGram){
    console.log(count)
  }
}
// END Array Histogram

// Object Histogram
async objectHistogram(){
  const file = await fetch(this._file_path);
  const fileText = await file.text()
  fileText.then
  const newlineCleaner =fileText.replace('\n',"");
  const periodCleaner = newlineCleaner.replace('.','');
  const commaCleaner = periodCleaner.replace(',','');
  const split = commaCleaner.split(' ');
  // console.log(split)
  const arrayGram = [];

  split.forEach( word =>  arrayGram.push(counterObj(split,word)))
  Object.entries(arrayGram).forEach(([key, val]) => {
      console.log(val);        // the value of the current key.
    });

}

// End  Histogram Class
}
