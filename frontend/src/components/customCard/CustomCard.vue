<template> 
    <div class="card-all">
        <div class="custom-card">
            <div class="content-card">
                <div>
                    <div class="card-header">
                        <div class="header__left">
                            <span>#{{id}}</span>
                        </div>
                        <div class="header__right">
                            <Icon v-if="type!='pdf'" iconName="refresh" className="a-button__icon" @click="front = !front"/>
                            <Icon iconName="fullscreen" className="a-button__icon" @click="showPopUp = true"/>
                            <div v-if="dateRead!=='no'" :class="['dot-status', [dateRead ? '-on' : '-off' ]]" :data-text="'Lido em '+ dateRead"></div>
                        </div>
                    </div>
                    <div class="card-body">
                        <div :class="['content-body__front', [{'-face': front}]]">
                            <div class="text">
                                <h5 class="title">{{title}}</h5>
                                <p v-if="textFront">{{textFront}}</p>
                                <p v-else>Nenhum texto.</p>
                            </div>
                            
                        </div>
                        <div v-if="type!='pdf'" :class="['content-body__back', [{'-face': !front}]]">
                            <div class="text">
                                <h5 class="title">{{title}}</h5>
                                <p>{{textBack}}</p>
                            </div>
                            
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <Box v-if="havePopUp" :show="showPopUp">
            <div v-if="type!='pdf'" class="custom-card -popUp">
                <div class="content-card">
                    <div>
                        <div class="card-header">
                            <div class="header__left">
                                <span>#{{id}}</span>
                            </div>
                            <div class="header__right">
                                <Icon iconName="refresh" className="a-button__icon" @click="frontPopUp = !frontPopUp"/>
                                <Icon iconName="close" className="a-button__icon" @click="showPopUp = false"/>
                                <div v-if="dateRead!=='no'" :class="['dot-status', [dateRead ? '-on' : '-off' ]]" :data-text="'Lido em '+ dateRead"></div>
                            </div>
                        </div>
                        <div class="card-body">
                            <div :class="['content-body__front', [{'-face': frontPopUp}]]">
                                <div class="text">
                                    <h5 class="title">{{title}}</h5>
                                    <p v-if="textFront">{{textFront}}</p>
                                    <p v-else>Nenhum texto.</p>
                                    <img class="img-card" v-if="frontImg" :src="`${this.apiURL}` + frontImg" alt="">
                                </div>

                            </div>
                            <div :class="['content-body__back', [{'-face': !frontPopUp}]]">
                                <div class="text">
                                    <h5 class="title">{{title}}</h5>
                                    <p>{{textBack}}</p>
                                    <img class="img-card" v-if="backImg" :src="`${this.apiURL}` + backImg" alt="">
                                </div>

                            </div>       
                        </div>
                    </div>
                </div>
            </div>
            <div v-else class="pdf-viewer">
                <Icon iconName="close" className="a-button__icon" @click="showPopUp = false"/>
                <embed v-if="showPopUp" :src="apiURL+pdfPath.concat('#toolbar=0&scrollbars=0&navpanes=0&zoom=100&scrollbar=0')" type="application/pdf">
            </div>
        </Box>
    </div>
</template>

<script>
import Icon from '@/components/icon/Icon.vue';
import Box from '@/components/box/Box.vue';

export default {
    data: function() {
        return {
            front: true,
            frontPopUp: true,
            showPopUp: false,
            teste : this.apiURL
        }
    },
    props: [ 'id', 'title', 'textFront', 'textBack', 'frontImg', 'backImg','dateRead', 'havePopUp', 'type', 'pdfPath' ],
    components: {
        Icon,
        Box,
    },
}
</script>

<style src="./customCard.scss" lang="scss"></style>