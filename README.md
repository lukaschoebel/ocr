# OCR

The objective of this repository is to understand common techniques for extracting text from handwritten documents. In general, the goal is to obtain the text from transcribed German letters from the beginning of the 20th century.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Requirements](#requirements)
- [Learnings](#learnings)
- [Acknowledgements](#acknowledgements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Requirements

- `pytesseract` and [`tesseract`](https://github.com/tesseract-ocr/tesseract)
- `openCV`

## Learnings

In the beginning, the use of `tesseract` was evaluated but it was found out that the library only performs reasonably well when the data is not noisy and machine written.

## Acknowledgements

- Kudos to Adrian Rosebrocks and his [OCR Tutorial](https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/)
