package letter

import (
	"sync"
)

// FreqMap records the frequency of each rune in a given text.
type FreqMap map[rune]int

// Frequency counts the frequency of each rune in a given text and returns this
// data as a FreqMap.
func Frequency(s string) FreqMap {
	m := FreqMap{}
	for _, r := range s {
		m[r]++
	}
	return m
}

func ConcurrentFrequency(list []string) FreqMap {
	var s sync.WaitGroup
	m := FreqMap{}
	ch := make(chan FreqMap, len(list))

	for _, item := range list {
		s.Add(1)
		go func(text string, ch chan<- FreqMap, wg *sync.WaitGroup) {
			defer wg.Done()
			ch <- Frequency(text)
		}(item, ch, &s)
	}

	s.Wait()
	close(ch)

	for item := range ch {
		for k, v := range item {
			m[k] += v
		}
	}

	return m
}
