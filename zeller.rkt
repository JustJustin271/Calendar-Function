#lang racket
(require rackunit)
;;NOT USING BEGINNER STUDENT LANGUAGE, USE FULL RACKET LANG

(define-struct date (month day year))
(define days (list "Saturday" "Sunday" "Monday" "Tuesday" "Wednesday" "Thursday" "Friday"))
;;Racket already assigns them an invisible number, starting at 0 to 6

;;Dates
(define orange (make-date 1 1 1970))
(define banana (make-date 5 27 2011))
(define melon (make-date 7 2 1992))
(define kiwi (make-date 10 20 2010))
(define strawberry (make-date 5 6 2011))
(define blueberry (make-date 10 1 2011))
(define cantelope (make-date 2 13 2011))

;; Zeller's Congruence Formula:
;; h = (q + floor(13(m+1)/5) + K + floor(K/4) + floor(J/4) - 2J) mod 7

;; Variable Definitions:
;; h = Day of the week (0 = Saturday, 1 = Sunday, ..., 6 = Friday)
;; q = Day of the month
;; m = Adjusted Month (March = 3, ..., December = 12; Jan = 13, Feb = 14)
;; Y = Adjusted Year (If Month < 3, Year = Year - 1)
;; K = Year of the century (Y mod 100)
;; J = Zero-based century (floor(Y / 100))
;;**Taken off of the internet :)**

;;January is 13th month, February is 14th, March is 3rd
;; 1/1/70 -> 13/1/69
;; First Month of 1970 is the 13th month of 1969

;; date -> int
;; Applies Zeller Formula to calculate the nth day of the week
;; Of a given date
(define (zeller apple)
  (let*(
    [month-raw (date-month apple)] ;;Raw Month
    [year-raw (date-year apple)] ;;Raw Year

    [month (if (< month-raw 3) (+ month-raw 12) month-raw)] ;;Processed Month
    [year  (if (< month-raw 3) (sub1 year-raw) year-raw)] ;;Processed Year

    [day (date-day apple)] ;;Also known as 
    [k (modulo year 100)] ;;last 2 digits
    [j (quotient year 100)] ;;first 2 digits

    [part-1 day]
    [part-2 (quotient (* 13 (add1 month)) 5)]
    [part-3 k]
    [part-4 (quotient k 4)]
    [part-5 (quotient j 4)]
    [part-6 (* -2 j)])

  (modulo (+ part-1 part-2 part-3 part-4 part-5 part-6) 7)))

(check-equal? (zeller blueberry) 0)
(check-equal? (zeller strawberry) 6)
(check-equal? (zeller cantelope) 1)
(check-equal? (zeller banana) 6)

;; day-of-week : date -> string
;; Takes in a date and outputs the day of the week
;; That date was on
(define (day-of-week date)
  (list-ref days (zeller date)))

(check-equal? (day-of-week orange) "Thursday")
(check-equal? (day-of-week kiwi) "Wednesday")
(check-equal? (day-of-week melon) "Thursday")

    
;;March 19th, 2026
;;This is a cool function to use :)
;;It works presumably most of the time :D
;;Zeller was a cool dude for making this cool function
;;Now, we can track dates going far back like the 90's ;) 
    
